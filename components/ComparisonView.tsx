'use client'

import { useState } from 'react'
import { api, type OptionParams } from '@/lib/api'

export default function ComparisonView() {
  const [params, setParams] = useState<OptionParams>({
    spotPrice: 100,
    strikePrice: 100,
    timeToMaturity: 1,
    riskFreeRate: 0.05,
    volatility: 0.2,
    optionType: 'call'
  })
  const [results, setResults] = useState<any>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleCompare = async () => {
    setLoading(true)
    setError(null)
    try {
      const data = await api.compareModels(params)
      setResults(data)
    } catch (err: any) {
      setError(err.response?.data?.error || 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      {/* Input Section */}
      <div className="card">
        <h2 className="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Compare Models</h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div>
            <label className="label">Option Type</label>
            <select
              value={params.optionType}
              onChange={(e) => setParams({ ...params, optionType: e.target.value as 'call' | 'put' })}
              className="input-field"
            >
              <option value="call">Call</option>
              <option value="put">Put</option>
            </select>
          </div>
          <div>
            <label className="label">Spot Price</label>
            <input
              type="number"
              value={params.spotPrice}
              onChange={(e) => setParams({ ...params, spotPrice: parseFloat(e.target.value) })}
              className="input-field"
              step="0.01"
            />
          </div>
          <div>
            <label className="label">Strike Price</label>
            <input
              type="number"
              value={params.strikePrice}
              onChange={(e) => setParams({ ...params, strikePrice: parseFloat(e.target.value) })}
              className="input-field"
              step="0.01"
            />
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div>
            <label className="label">Time to Maturity (years)</label>
            <input
              type="number"
              value={params.timeToMaturity}
              onChange={(e) => setParams({ ...params, timeToMaturity: parseFloat(e.target.value) })}
              className="input-field"
              step="0.01"
            />
          </div>
          <div>
            <label className="label">Risk-Free Rate</label>
            <input
              type="number"
              value={params.riskFreeRate}
              onChange={(e) => setParams({ ...params, riskFreeRate: parseFloat(e.target.value) })}
              className="input-field"
              step="0.001"
            />
          </div>
          <div>
            <label className="label">Volatility</label>
            <input
              type="number"
              value={params.volatility}
              onChange={(e) => setParams({ ...params, volatility: parseFloat(e.target.value) })}
              className="input-field"
              step="0.01"
            />
          </div>
        </div>

        <button
          onClick={handleCompare}
          disabled={loading}
          className="btn-primary w-full"
        >
          {loading ? 'Comparing...' : 'Compare All Models'}
        </button>

        {error && (
          <div className="mt-4 p-3 bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-200 rounded">
            {error}
          </div>
        )}
      </div>

      {/* Results Section */}
      {results && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Black-Scholes */}
          <div className="card bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/30 dark:to-blue-800/30">
            <h3 className="text-xl font-bold mb-4 text-blue-800 dark:text-blue-300">Black-Scholes</h3>
            <div className="mb-4 p-3 bg-white dark:bg-gray-800 rounded">
              <p className="text-sm text-gray-600 dark:text-gray-400">Price</p>
              <p className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                ${results.black_scholes?.price?.toFixed(4)}
              </p>
            </div>
            <div className="space-y-2">
              <h4 className="font-semibold text-sm text-gray-700 dark:text-gray-300">Greeks</h4>
              {results.black_scholes?.greeks && (
                <div className="grid grid-cols-2 gap-2 text-sm">
                  <div className="p-2 bg-white dark:bg-gray-800 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Delta</p>
                    <p className="font-semibold">{results.black_scholes.greeks.delta?.toFixed(4)}</p>
                  </div>
                  <div className="p-2 bg-white dark:bg-gray-800 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Gamma</p>
                    <p className="font-semibold">{results.black_scholes.greeks.gamma?.toFixed(4)}</p>
                  </div>
                  <div className="p-2 bg-white dark:bg-gray-800 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Vega</p>
                    <p className="font-semibold">{results.black_scholes.greeks.vega?.toFixed(4)}</p>
                  </div>
                  <div className="p-2 bg-white dark:bg-gray-800 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Theta</p>
                    <p className="font-semibold">{results.black_scholes.greeks.theta?.toFixed(4)}</p>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Binomial Tree */}
          <div className="card bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/30 dark:to-green-800/30">
            <h3 className="text-xl font-bold mb-4 text-green-800 dark:text-green-300">Binomial Tree</h3>
            <div className="mb-4 p-3 bg-white dark:bg-gray-800 rounded">
              <p className="text-sm text-gray-600 dark:text-gray-400">Price</p>
              <p className="text-2xl font-bold text-green-600 dark:text-green-400">
                ${results.binomial_tree?.price?.toFixed(4)}
              </p>
            </div>
            <div className="space-y-2">
              <h4 className="font-semibold text-sm text-gray-700 dark:text-gray-300">Greeks</h4>
              <div className="grid grid-cols-2 gap-2 text-sm">
                <div className="p-2 bg-white dark:bg-gray-800 rounded">
                  <p className="text-xs text-gray-600 dark:text-gray-400">Delta</p>
                  <p className="font-semibold">{results.binomial_tree?.delta?.toFixed(4)}</p>
                </div>
                <div className="p-2 bg-white dark:bg-gray-800 rounded">
                  <p className="text-xs text-gray-600 dark:text-gray-400">Gamma</p>
                  <p className="font-semibold">{results.binomial_tree?.gamma?.toFixed(4)}</p>
                </div>
              </div>
            </div>
          </div>

          {/* Monte Carlo */}
          <div className="card bg-gradient-to-br from-purple-50 to-purple-100 dark:from-purple-900/30 dark:to-purple-800/30">
            <h3 className="text-xl font-bold mb-4 text-purple-800 dark:text-purple-300">Monte Carlo</h3>
            <div className="mb-4 p-3 bg-white dark:bg-gray-800 rounded">
              <p className="text-sm text-gray-600 dark:text-gray-400">Price</p>
              <p className="text-2xl font-bold text-purple-600 dark:text-purple-400">
                ${results.monte_carlo?.price?.toFixed(4)}
              </p>
            </div>
            <div className="space-y-2">
              <h4 className="font-semibold text-sm text-gray-700 dark:text-gray-300">Confidence Interval (95%)</h4>
              {results.monte_carlo?.confidence_interval && (
                <div className="p-2 bg-white dark:bg-gray-800 rounded text-sm">
                  <p>
                    [{results.monte_carlo.confidence_interval[0]?.toFixed(4)},
                    {results.monte_carlo.confidence_interval[1]?.toFixed(4)}]
                  </p>
                  <p className="text-xs text-gray-600 dark:text-gray-400 mt-1">
                    Std Error: {results.monte_carlo.std_error?.toFixed(6)}
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
