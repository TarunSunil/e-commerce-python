/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        display: ['Bricolage Grotesque', 'Noto Sans', 'sans-serif'],
        body: ['Instrument Sans', 'Noto Sans', 'sans-serif'],
      },
      colors: {
        meridian: {
          bg: 'var(--bg)',
          surface: 'var(--sf)',
          ink: 'var(--ink)',
          muted: 'var(--mu)',
          brand: 'var(--br)',
          deep: 'var(--bx)',
          highlight: 'var(--hi)',
          sale: 'var(--sa)',
        },
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [],
}
