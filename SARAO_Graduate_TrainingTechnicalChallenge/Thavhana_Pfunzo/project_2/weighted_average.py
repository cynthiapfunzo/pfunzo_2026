from typing import List
from collections import deque

class WeightedAverage:
    """
    A class that provides a weighted sum average of the last n entries of a digitized signal.
    
    The weighted average is calculated as:
    y[n] = (w[0]*x[0] + w[1]*x[1] + ... + w[n-1]*x[n-1]) / n
    
    where x holds the last n entries, with index 0 being the most recent entry.
    """
    
    def __init__(self, w: List[float]):
        """
        Initialize the WeightedAverage with the given weights.
        
        Args:
            w (List[float]): List of weights for the moving average
            
        Raises:
            ValueError: If weights list is empty or contains all zeros
        """
        if not w:
            raise ValueError("Weights list cannot be empty")
            
        if all(weight == 0 for weight in w):
            raise ValueError("Weights cannot be all zeros")
            
        self.weights = w
        self.window_size = len(w)
        self.buffer = deque(maxlen=self.window_size)
        
        # Initialize buffer with zeros
        for _ in range(self.window_size):
            self.buffer.appendleft(0.0)
    
    def process(self, x: float) -> float:
        """
        Process a new value and return the current weighted average.
        
        Args:
            x (float): The new input value
            
        Returns:
            float: The current weighted average
        """
        # Add new value to the front of the buffer
        self.buffer.appendleft(x)
        
        # Calculate weighted sum
        weighted_sum = sum(w * x for w, x in zip(self.weights, self.buffer))
        
        # Calculate average (divide by number of weights)
        return weighted_sum / self.window_size


def generate_sine_wave(samples: int, frequency: float = 1.0, amplitude: float = 1.0) -> List[float]:
    """
    Generate a sine wave signal.
    
    Args:
        samples (int): Number of samples to generate
        frequency (float): Frequency of the sine wave in Hz
        amplitude (float): Amplitude of the sine wave
        
    Returns:
        List[float]: Generated sine wave samples
    """
    import math
    # For 2Hz frequency, we need exactly 2 full cycles in the output
    # Each sample is i/samples of the total time, multiplied by 2*pi*frequency to get radians
    return [amplitude * math.sin(2 * math.pi * frequency * i / samples * 2) 
            for i in range(samples)]

def main():
    # Example usage with the given test case
    weights = [5, 4, 3, 2, 1]
    signal = [1, 2, 3, 4, 5]
    
    print("Test case:")
    print(f"Weights: {weights}")
    print(f"Signal: {signal}")
    
    wa = WeightedAverage(weights)
    
    # Process each value in the signal
    for x in signal:
        result = wa.process(x)
        
    print(f"Final weighted average: {result:.1f}")
    
    # Example with sine wave and moving average (all weights = 1)
    print("\nExample with sine wave and moving average (all weights = 1):")
    window_size = 5
    weights = [1] * window_size
    wa = WeightedAverage(weights)
    
    # Generate a sine wave
    sine_wave = generate_sine_wave(samples=20, frequency=2.0, amplitude=1.0)
    
    print("\nSample  Value    Moving Average")
    print("-" * 35)
    for i, x in enumerate(sine_wave):
        avg = wa.process(x)
        print(f"{i:4d}   {x:6.3f}    {avg:10.6f}")


if __name__ == "__main__":
    main()
