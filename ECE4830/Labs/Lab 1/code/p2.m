load('ACsig.mat')

fs = 25000;
x_axis = linspace(0, length(x)/fs, length(x)); % Generate x-axis values based on sampling frequency

figure;
plot(x_axis, x); % Plot the signal with time on the x-axis
xlabel('Time (s)'); % Label the x-axis
ylabel('Amplitude'); % Label the y-axis
title('AC Signal - Time scale'); % Add a title
exportgraphics(gcf, 'signal.png', Resolution=600);

% Compute the FFT
N = length(x);
X = fft(x);

% Plot in real frequency with units of Hz
f_axis = linspace(0, fs, N);
figure;
plot(f_axis, abs(X)); % Plot the magnitude of the FFT
xlabel('Frequency (Hz)'); % Label the x-axis
ylabel('Magnitude'); % Label the y-axis
title('AC Signal - Frequency scale'); % Add a title
exportgraphics(gcf, 'fft.png', Resolution=600);