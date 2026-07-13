/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './js/**/*.js'],
  theme: {
    extend: {
      colors: {
        void: {
          DEFAULT: '#050810',
          50: '#0a0f1a',
          100: '#0d1220',
          200: '#111827',
          300: '#1a2235',
        },
        electric: {
          DEFAULT: '#00d4ff',
          dim: '#00a8cc',
          glow: '#33e0ff',
        },
        plasma: {
          DEFAULT: '#7c3aed',
          dim: '#6d28d9',
          glow: '#a78bfa',
        },
        signal: {
          DEFAULT: '#3b82f6',
          dim: '#2563eb',
        },
        // AAE aperture family (aligns with household app)
        amber: {
          DEFAULT: '#f5b942',
          dim: '#e8a317',
          glow: '#ffd06a',
        },
        gold: {
          DEFAULT: '#e8a317',
        },
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        body: ['"Inter"', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      backgroundImage: {
        'grid-pattern':
          'linear-gradient(rgba(0, 212, 255, 0.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0, 212, 255, 0.03) 1px, transparent 1px)',
        'hero-gradient':
          'radial-gradient(ellipse 80% 60% at 50% -20%, rgba(0, 212, 255, 0.15), transparent), radial-gradient(ellipse 60% 50% at 80% 50%, rgba(124, 58, 237, 0.12), transparent)',
        'card-glow':
          'linear-gradient(135deg, rgba(0, 212, 255, 0.08) 0%, rgba(124, 58, 237, 0.08) 100%)',
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
          '0 0 40px rgba(0, 212, 255, 0.15), 0 0 80px rgba(0, 212, 255, 0.05)',
        plasma:
          '0 0 40px rgba(124, 58, 237, 0.15), 0 0 80px rgba(124, 58, 237, 0.05)',
        amber:
          '0 0 40px rgba(245, 185, 66, 0.18), 0 0 80px rgba(232, 163, 23, 0.06)',
        card: '0 4px 24px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.04)',
      },
    },
  },
  plugins: [],
};
