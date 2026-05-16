export default function ProcessingControls({
  target,
  setTarget,
  unit,
  setUnit,
  operation,
  setOperation,
  onProcess,
  loading
}) {
  return (
    <div className="controls-card glass-card fade-in">
      <div className="input-group">
        <label>Target Size</label>

        <input
          type="number"
          value={target}
          onChange={(e) => setTarget(e.target.value)}
          placeholder="Enter target size"
        />
      </div>

      <div className="input-group">
        <label>Size Unit</label>

        <select
          value={unit}
          onChange={(e) => setUnit(e.target.value)}
        >
          <option value="KB" style={{color : "black"}}>KB</option>
          <option value="MB" style={{color : "black"}}>MB</option>
        </select>
      </div>

      <div className="input-group">
        <label>Operation</label>

        <select
          value={operation}
          onChange={(e) => setOperation(e.target.value)}
        >
          <option value="decrease" style={{color: "black"}}>Decrease</option>
          <option value="increase" style={{color : "black"}}>Increase</option>
        </select>
      </div>

      <button
        className="primary-btn"
        onClick={onProcess}
        disabled={loading}
      >
        {loading ? 'Processing...' : 'Process File'}
      </button>
    </div>
  )
}