import { Component, ErrorInfo, ReactNode } from 'react';

interface ErrorBoundaryProps {
  children: ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
}

export class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  state: ErrorBoundaryState = { hasError: false };

  static getDerivedStateFromError(): ErrorBoundaryState {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error('Unhandled UI error:', error, info);
  }

  handleRetry = () => {
    this.setState({ hasError: false });
  };

  render() {
    if (!this.state.hasError) return this.props.children;

    return (
      <main className="mx-auto flex min-h-[60vh] max-w-xl flex-col items-center justify-center px-6 text-center">
        <h1 className="text-3xl font-bold text-gray-900">Something went wrong</h1>
        <p className="mt-3 text-gray-600">We could not display this page. Please try again.</p>
        <button
          type="button"
          onClick={this.handleRetry}
          className="mt-6 rounded-lg bg-primary-600 px-5 py-3 font-semibold text-white hover:bg-primary-700"
        >
          Retry
        </button>
      </main>
    );
  }
}
