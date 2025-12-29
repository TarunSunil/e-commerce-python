# Contributing to E-Commerce Management System

Thank you for your interest in contributing to the E-Commerce Management System! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/e-commerce-python.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

### Backend Development

1. Set up the development environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-test.txt
```

2. Run tests:
```bash
pytest
```

3. Start the development server:
```bash
uvicorn app.main:app --reload
```

### Frontend Development

1. Set up the development environment:
```bash
cd frontend
npm install
```

2. Run tests:
```bash
npm test
```

3. Start the development server:
```bash
npm start
```

## Code Style

### Python (Backend)
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small
- Use meaningful variable and function names

### JavaScript/React (Frontend)
- Use functional components with hooks
- Follow React best practices
- Use meaningful component and variable names
- Keep components focused and reusable
- Use proper prop types or TypeScript

## Testing

- Write tests for new features
- Ensure all tests pass before submitting a PR
- Aim for good test coverage
- Test both success and error cases

## Pull Request Guidelines

1. **Title**: Use a clear and descriptive title
2. **Description**: Explain what changes you made and why
3. **Testing**: Describe how you tested your changes
4. **Screenshots**: Include screenshots for UI changes
5. **Breaking Changes**: Clearly mark any breaking changes

## Commit Message Guidelines

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

## Feature Requests and Bug Reports

### Bug Reports

When reporting bugs, please include:
- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment details (OS, browser, etc.)

### Feature Requests

When requesting features, please include:
- A clear and descriptive title
- Detailed description of the feature
- Use cases and benefits
- Possible implementation approach (optional)

## Code Review Process

1. All submissions require review
2. Maintainers will review your PR
3. Address any feedback or requested changes
4. Once approved, your PR will be merged

## Community

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

## Questions?

If you have questions, feel free to:
- Open an issue for discussion
- Reach out to the maintainers

Thank you for contributing! 🎉
