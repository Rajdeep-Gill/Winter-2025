% Define the number of samples to compute
N = 10; 

% Define impulse input
x = [1, zeros(1, N-1)];

% First system: y1(n) - 0.5*y1(n-1) = 2*x(n)
b1 = [2];
a1 = [1, -0.5];
h1 = filter(b1, a1, x);

% Second system: h2(n) = (1/4)^n * u(n)
n = 0:N-1;
h2 = (1./(4.^n));

% Compute total impulse response
h = h1 + h2;

% Display first three samples
fprintf('h(0) = %.4f\n', h(1));
fprintf('h(1) = %.4f\n', h(2));
fprintf('h(2) = %.4f\n', h(3));

% Plot impulse responses
stem(0:N-1, h, 'filled');
xlabel('n');
ylabel('h(n)');
title('Impulse Response of the System');
grid on;
