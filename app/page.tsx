'use client'

import { useState } from 'react'
import OptionsCalculator from '@/components/OptionsCalculator'
import ComparisonView from '@/components/ComparisonView'
import VisualizationPanel from '@/components/VisualizationPanel'

export default function Home() {
  const [activeTab, setActiveTab] = useState<'calculator' | 'comparison' | 'visualization'>('calculator')

  return (
    <main className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 dark:from-gray-900 dark:to-gray-800">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <header className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 dark:text-white mb-2">
            Options Pricing Models
          </h1>
          <p className="text-gray-600 dark:text-gray-300">
            Advanced pricing using Black-Scholes, Binomial Tree, and Monte Carlo methods
          </p>
        </header>

        {/* Tab Navigation */}
        <div className="flex justify-center mb-8">
          <div className="inline-flex rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 p-1">
            <button
              onClick={() => setActiveTab('calculator')}
              className={`px-6 py-2 rounded-md font-medium transition-colors ${
                activeTab === 'calculator'
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
              }`}
            >
              Calculator
            </button>
            <button
              onClick={() => setActiveTab('comparison')}
              className={`px-6 py-2 rounded-md font-medium transition-colors ${
                activeTab === 'comparison'
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
              }`}
            >
              Comparison
            </button>
            <button
              onClick={() => setActiveTab('visualization')}
              className={`px-6 py-2 rounded-md font-medium transition-colors ${
                activeTab === 'visualization'
                  ? 'bg-blue-600 text-white'
                  : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'
              }`}
            >
              Visualization
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="max-w-7xl mx-auto">
          {activeTab === 'calculator' && <OptionsCalculator />}
          {activeTab === 'comparison' && <ComparisonView />}
          {activeTab === 'visualization' && <VisualizationPanel />}
        </div>

        {/* Footer */}
        <footer className="text-center mt-12 text-gray-600 dark:text-gray-400 text-sm">
          <p>Built with Python (Flask), Next.js, and Tailwind CSS</p>
        </footer>
      </div>
    </main>
  )
}
