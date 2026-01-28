import pytest
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from project_2.weighted_average import WeightedAverage, generate_sine_wave

class TestWeightedAverage:
    def test_initialization(self):
        """Test WeightedAverage initialization with different weight configurations"""
        # Test with valid weights
        weights = [0.5, 0.3, 0.2]
        wa = WeightedAverage(weights)
        assert wa.weights == weights
        assert wa.window_size == len(weights)
        
        # Test with equal weights (moving average)
        weights = [1, 1, 1, 1]
        wa = WeightedAverage(weights)
        assert wa.weights == weights
    
    def test_process_basic(self):
        """Test the process method with basic input sequence"""
        weights = [0.5, 0.3, 0.2]
        wa = WeightedAverage(weights)
        
        # First value (buffer not full yet)
        result = wa.process(10)
        expected = (10 * 0.5) / 3  # Only first weight is used, but divided by total weights
        assert np.isclose(result, expected)
        
        # Second value
        result = wa.process(20)
        expected = (20 * 0.5 + 10 * 0.3) / 3
        assert np.isclose(result, expected)
        
        # Third value (buffer now full)
        result = wa.process(30)
        expected = (30 * 0.5 + 20 * 0.3 + 10 * 0.2) / 3
        assert np.isclose(result, expected)
        
        # Fourth value (buffer slides)
        result = wa.process(40)
        expected = (40 * 0.5 + 30 * 0.3 + 20 * 0.2) / 3
        assert np.isclose(result, expected)
    
    def test_moving_average(self):
        """Test with equal weights (simple moving average)"""
        window_size = 5
        weights = [1] * window_size
        wa = WeightedAverage(weights)
        
        # Test with increasing values
        values = [1, 2, 3, 4, 5, 6, 7]
        expected = [0.2, 0.6, 1.2, 2.0, 3.0, 4.0, 5.0]  # Sum / 5
        
        for v, e in zip(values, expected):
            result = wa.process(v)
            assert np.isclose(result, e, atol=1e-10)
    
    def test_negative_weights(self):
        """Test with negative weights"""
        weights = [1, -0.5, 0.5]
        wa = WeightedAverage(weights)
        
        # Fill the buffer
        wa.process(10)
        wa.process(20)
        result = wa.process(30)
        
        expected = (30 * 1 + 20 * -0.5 + 10 * 0.5) / 3
        assert np.isclose(result, expected)
    
    def test_single_weight(self):
        """Test with a single weight (should just scale the input)"""
        weights = [2.5]
        wa = WeightedAverage(weights)
        
        result = wa.process(10)
        assert np.isclose(result, 10 * 2.5 / 1.0)
        
        result = wa.process(20)
        assert np.isclose(result, 20 * 2.5 / 1.0)
    
    def test_generate_sine_wave(self):
        """Test the sine wave generator function"""
        samples = 100
        frequency = 2.0
        amplitude = 1.5
        
        wave = generate_sine_wave(samples, frequency, amplitude)
        
        # Check output shape and type
        assert len(wave) == samples
        assert isinstance(wave[0], float)
        
        # Check amplitude
        assert np.all(np.abs(wave) <= amplitude + 1e-10)
        
        # Check frequency (should complete 2 full cycles in 100 samples)
        zero_crossings = np.where(np.diff(np.signbit(wave)))[0]
        assert len(zero_crossings) == 4  # 2 full cycles = 4 zero crossings
        
        # Check periodicity
        period = samples / frequency
        assert np.allclose(wave[0], wave[int(period)], atol=1e-10)

class TestEdgeCases:
    def test_empty_weights(self):
        """Test with empty weights (should raise an error)"""
        with pytest.raises(ValueError):
            WeightedAverage([])
    
    def test_zero_weights(self):
        """Test with all zero weights (should raise an error)"""
        with pytest.raises(ValueError):
            WeightedAverage([0, 0, 0])
    
    def test_non_numeric_input(self):
        """Test with non-numeric input (should raise an error)"""
        wa = WeightedAverage([1, 1])
        with pytest.raises(TypeError):
            wa.process("not a number")

if __name__ == "__main__":
    pytest.main()
