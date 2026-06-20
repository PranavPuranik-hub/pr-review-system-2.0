const { greet } = require('../src/App');

test('greet returns correct string', () => {
  expect(greet('World')).toBe('Hello, World');
});