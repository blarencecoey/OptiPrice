'use client'

import { useState } from 'react'
import { api, type OptionParams } from '@/lib/api'

export default function VisualizationPanel() {
  const [visualType, setVisualType] = useState<'price-vs-spot' | 'greeks' | 'monte-carlo'>('price-vs-spot')
  const [params, setParams] = useState<OptionParams>({
    spotPrice: 100,
    strikePrice: 100,
    timeToMaturity: 1,
    riskFreeRate: 0.05,
    volatility: 0.2,
    optionType: 'call'
  })
  const [model, setModel] = useState<'black-scholes' | 'binomial-tree' | 'monte-carlo'>('black-scholes')
  const [imageData, setImageData] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleGenerate = async () => {
    setLoading(true)
    setError(null)
    try {
      let data
      if (visualType === 'price-vs-spot') {
        data = await api.visualizePriceVsSpot({
          ...params,
          model: model,
          spotMin: params.strikePrice * 0.5,
          spotMax: params.strikePrice * 1.5
        })
      } else if (visualType === 'greeks') {
        data = await api.visualizeGreeks({
          ...params,
          spotMin: params.strikePrice * 0.5,
          spotMax: params.strikePrice * 1.5
        })
      } else {
        data = await api.visualizeMonteCarloPaths({
          ...params,
          numPaths: 100
        })
      }
      setImageData(data.image)
    } catch (err: any) {
      setError(err.response?.data?.error || 'An error occurred')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      {/* Controls */}
      <div className="card">
        <h2 className="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Visualization</h2>

        {/* Visualization Type */}
        <div className="mb-6">
          <label className="label">Visualization Type</label>
          <select
            value={visualType}
            onChange={(e) => setVisualType(e.target.value as any)}
            className="input-field"
          >
            <option value="price-vs-spot">Option Price vs Spot Price</option>
            <option value="greeks">Greeks Analysis</option>
            <option value="monte-carlo">Monte Carlo Paths</option>
          </select>
        </div>

        {/* Model Selection (for price-vs-spot) */}
        {visualType === 'price-vs-spot' && (
          <div className="mb-4">
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
        )}

        {/* Parameters Grid */}
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
          onClick={handleGenerate}
          disabled={loading}
          className="btn-primary w-full"
        >
          {loading ? 'Generating...' : 'Generate Visualization'}
        </button>

        {error && (
          <div className="mt-4 p-3 bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-200 rounded">
            {error}
          </div>
        )}
      </div>

      {/* Visualization Display */}
      {imageData && (
        <div className="card">
          <img
            src={`data:image/png;base64,${imageData}`}
            alt="Visualization"
            className="w-full rounded-lg"
          />
        </div>
      )}

      {!imageData && !loading && (
        <div className="card text-center text-gray-500 dark:text-gray-400 py-12">
          <p>Configure parameters and click Generate to see visualization</p>
        </div>
      )}
    </div>
  )
}
