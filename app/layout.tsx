import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Options Pricing Models',
  description: 'Advanced options pricing using Black-Scholes, Binomial Tree, and Monte Carlo methods',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
