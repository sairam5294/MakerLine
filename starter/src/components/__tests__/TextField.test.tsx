import { render, screen } from '@testing-library/react-native';
import { TextField } from '../TextField';

describe('TextField', () => {
  it('has a visible label that also names the input', async () => {
    await render(<TextField label="Email" value="" onChangeText={() => {}} />);
    expect(screen.getByText('Email')).toBeOnTheScreen();
    expect(screen.getByLabelText('Email')).toBeOnTheScreen();
  });

  it('shows errors as an alert so screen readers announce them', async () => {
    await render(
      <TextField label="Email" value="x" onChangeText={() => {}} error="Enter a valid email." />,
    );
    expect(screen.getByRole('alert')).toHaveTextContent('Enter a valid email.');
  });
});
