/** @type {import('tailwindcss').Config} */
/** experiment/brand-copy — stamp, don't stream (light professional room) */
module.exports = {
  content: [
    './index.html',
    './solo/**/*.html',
    './enterprise/**/*.html',
    './partials/**/*.html',
    './js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        // Paper / ink canvas (was cyber void)
        // Uniform light-gray canvas (white cards + mark primaries sit on top)
        void: {
          DEFAULT: '#e8eaee',
          50: '#e8eaee',
          100: '#eef0f3',
          200: '#e0e3e9',
          300: '#d0d4dc',
        },
        // Trust steel-blue (was neon cyan) — token name kept for class compatibility
        electric: {
          DEFAULT: '#3b6f9e',
          dim: '#2f5a80',
          glow: '#5b8fbe',
        },
        // Quiet indigo (was plasma neon)
        plasma: {
          DEFAULT: '#5c6b8a',
          dim: '#4a5670',
          glow: '#7a8aab',
        },
        signal: {
          DEFAULT: '#4a7ab0',
          dim: '#3a6290',
        },
        // Muted brass (was neon amber)
        amber: {
          DEFAULT: '#b8954a',
          dim: '#9a7a38',
          glow: '#d4b06a',
        },
        gold: {
          DEFAULT: '#a6843c',
        },
        // Field + prose: pure black (sizes/fonts carry hierarchy, not mid-gray)
        ink: {
          DEFAULT: '#000000',
          soft: '#000000',
          muted: '#000000',
        },
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        body: ['"Inter"', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      backgroundImage: {
        'grid-pattern':
          'linear-gradient(rgba(59, 111, 158, 0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(59, 111, 158, 0.04) 1px, transparent 1px)',
        'hero-gradient':
          'radial-gradient(ellipse 80% 60% at 50% -20%, rgba(59, 111, 158, 0.08), transparent), radial-gradient(ellipse 60% 50% at 80% 50%, rgba(92, 107, 138, 0.06), transparent)',
        'card-glow':
          'linear-gradient(135deg, rgba(59, 111, 158, 0.04) 0%, rgba(92, 107, 138, 0.04) 100%)',
      },
      backgroundSize: {
        grid: '64px 64px',
      },
      animation: {
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        float: 'float 6s ease-in-out infinite',
        glow: 'glow 3s ease-in-out infinite alternate',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        glow: {
          '0%': { opacity: '0.4' },
          '100%': { opacity: '1' },
        },
      },
      boxShadow: {
        electric:
          '0 0 24px rgba(59, 111, 158, 0.1), 0 0 48px rgba(59, 111, 158, 0.04)',
        plasma:
          '0 0 24px rgba(92, 107, 138, 0.1), 0 0 48px rgba(92, 107, 138, 0.04)',
        amber:
          '0 0 24px rgba(184, 149, 74, 0.12), 0 0 48px rgba(166, 132, 60, 0.04)',
        card: '0 4px 20px rgba(45, 50, 60, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.8)',
      },
    },
  },
  plugins: [],
};
