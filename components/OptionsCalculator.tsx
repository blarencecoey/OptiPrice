'use client'

import { useState } from 'react'
import { api, type OptionParams } from '@/lib/api'

export default function OptionsCalculator() {
  const [model, setModel] = useState<'black-scholes' | 'binomial-tree' | 'monte-carlo'>('black-scholes')
  const [params, setParams] = useState<OptionParams>({
    spotPrice: 100,
    strikePrice: 100,
    timeToMaturity: 1,
    riskFreeRate: 0.05,
    volatility: 0.2,
    optionType: 'call'
  })
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleCalculate = async () => {
    setLoading(true)
    setError(null)
    try {
      let data
      if (model === 'black-scholes') {
        data = await api.priceBlackScholes(params)
      } else if (model === 'binomial-tree') {
        data = await api.priceBinomialTree({ ...params, steps: 100 })
      } else {
        data = await api.priceMonteCarlo({ ...params, simulations: 10000 })
      }
      setResult(data)
    } catch (err: any) {
      setError(err.response?.data?.error || 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
      {/* Input Panel */}
      <div className="card">
        <h2 className="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Options Parameters</h2>

        {/* Model Selection */}
        <div className="mb-6">
          <label className="label">Pricing Model</label>
          <select
            value={model}
            onChange={(e) => setModel(e.target.value as any)}
            className="input-field"
          >
            <option value="black-scholes">Black-Scholes</option>
            <option value="binomial-tree">Binomial Tree</option>
            <option value="monte-carlo">Monte Carlo</option>
          </select>
        </div>

        {/* Option Type */}
        <div className="mb-4">
          <label className="label">Option Type</label>
          <div className="flex gap-4">
            <label className="flex items-center">
              <input
                type="radio"
                value="call"
                checked={params.optionType === 'call'}
                onChange={(e) => setParams({ ...params, optionType: e.target.value as 'call' | 'put' })}
                className="mr-2"
              />
              Call
            </label>
            <label className="flex items-center">
              <input
                type="radio"
                value="put"
                checked={params.optionType === 'put'}
                onChange={(e) => setParams({ ...params, optionType: e.target.value as 'call' | 'put' })}
                className="mr-2"
              />
              Put
            </label>
          </div>
        </div>

        {/* Spot Price */}
        <div className="mb-4">
          <label className="label">Spot Price (S)</label>
          <input
            type="number"
            value={params.spotPrice}
            onChange={(e) => setParams({ ...params, spotPrice: parseFloat(e.target.value) })}
            className="input-field"
            step="0.01"
          />
        </div>

        {/* Strike Price */}
        <div className="mb-4">
          <label className="label">Strike Price (K)</label>
          <input
            type="number"
            value={params.strikePrice}
            onChange={(e) => setParams({ ...params, strikePrice: parseFloat(e.target.value) })}
            className="input-field"
            step="0.01"
          />
        </div>

        {/* Time to Maturity */}
        <div className="mb-4">
          <label className="label">Time to Maturity (years)</label>
          <input
            type="number"
            value={params.timeToMaturity}
            onChange={(e) => setParams({ ...params, timeToMaturity: parseFloat(e.target.value) })}
            className="input-field"
            step="0.01"
            min="0.01"
          />
        </div>

        {/* Risk-Free Rate */}
        <div className="mb-4">
          <label className="label">Risk-Free Rate (r)</label>
          <input
            type="number"
            value={params.riskFreeRate}
            onChange={(e) => setParams({ ...params, riskFreeRate: parseFloat(e.target.value) })}
            className="input-field"
            step="0.001"
          />
        </div>

        {/* Volatility */}
        <div className="mb-6">
          <label className="label">Volatility (σ)</label>
          <input
            type="number"
            value={params.volatility}
            onChange={(e) => setParams({ ...params, volatility: parseFloat(e.target.value) })}
            className="input-field"
            step="0.01"
          />
        </div>

        <button
          onClick={handleCalculate}
          disabled={loading}
          className="btn-primary w-full"
        >
          {loading ? 'Calculating...' : 'Calculate Price'}
        </button>

        {error && (
          <div className="mt-4 p-3 bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-200 rounded">
            {error}
          </div>
        )}
      </div>

      {/* Results Panel */}
      <div className="card">
        <h2 className="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Results</h2>

        {result ? (
          <div>
            {/* Option Price */}
            <div className="mb-6 p-4 bg-blue-50 dark:bg-blue-900/30 rounded-lg">
              <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400 mb-1">Option Price</h3>
              <p className="text-3xl font-bold text-blue-600 dark:text-blue-400">
                ${result.price?.toFixed(4)}
              </p>
            </div>

            {/* Monte Carlo Confidence Interval */}
            {model === 'monte-carlo' && result.confidenceInterval && (
              <div className="mb-6 p-4 bg-purple-50 dark:bg-purple-900/30 rounded-lg">
                <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400 mb-2">95% Confidence Interval</h3>
                <p className="text-lg">
                  [{result.confidenceInterval.lower.toFixed(4)}, {result.confidenceInterval.upper.toFixed(4)}]
                </p>
                <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
                  Std Error: {result.standardError?.toFixed(6)}
                </p>
              </div>
            )}

            {/* Greeks */}
            {result.greeks && (
              <div>
                <h3 className="text-lg font-semibold mb-3 text-gray-800 dark:text-white">Greeks</h3>
                <div className="grid grid-cols-2 gap-3">
                  <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Delta (Δ)</p>
                    <p className="text-lg font-semibold">{result.greeks.delta?.toFixed(4)}</p>
                  </div>
                  <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Gamma (Γ)</p>
                    <p className="text-lg font-semibold">{result.greeks.gamma?.toFixed(4)}</p>
                  </div>
                  <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Vega (ν)</p>
                    <p className="text-lg font-semibold">{result.greeks.vega?.toFixed(4)}</p>
                  </div>
                  <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Theta (Θ)</p>
                    <p className="text-lg font-semibold">{result.greeks.theta?.toFixed(4)}</p>
                  </div>
                  <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Rho (ρ)</p>
                    <p className="text-lg font-semibold">{result.greeks.rho?.toFixed(4)}</p>
                  </div>
                </div>
              </div>
            )}

            {/* Binomial/Monte Carlo Greeks */}
            {(model === 'binomial-tree' || model === 'monte-carlo') && result.delta !== undefined && (
              <div>
                <h3 className="text-lg font-semibold mb-3 text-gray-800 dark:text-white">Greeks</h3>
                <div className="grid grid-cols-2 gap-3">
                  <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                    <p className="text-xs text-gray-600 dark:text-gray-400">Delta (Δ)</p>
                    <p className="text-lg font-semibold">{result.delta?.toFixed(4)}</p>
                  </div>
                  {result.gamma !== undefined && (
                    <div className="p-3 bg-gray-50 dark:bg-gray-700 rounded">
                      <p className="text-xs text-gray-600 dark:text-gray-400">Gamma (Γ)</p>
                      <p className="text-lg font-semibold">{result.gamma?.toFixed(4)}</p>
                    </div>
                  )}
                </div>
              </div>
            )}
          </div>
        ) : (
          <div className="text-center text-gray-500 dark:text-gray-400 py-12">
            <p>Enter parameters and click Calculate to see results</p>
          </div>
        )}
      </div>
    </div>
  )
}
