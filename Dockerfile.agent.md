import React, { useState } from 'react';
import { motion } from 'framer-motion';

export default function App() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('http://localhost:8000/upload/photo', {
        method: 'POST',
        body: formData,
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold text-blue-900 mb-8">AI Warehouse Optimizer</h1>
      
      <div className="grid grid-cols-2 gap-8">
        {/* Upload Section */}
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-4">AI Item Detection</h2>
          <input 
            type="file" 
            onChange={(e) => setFile(e.target.files ? e.target.files[0] : null)}
            className="mb-4 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
          />
          <button 
            onClick={handleUpload}
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 w-full"
            disabled={loading}
          >
            {loading ? "Analyzing with Gemini..." : "Upload & Analyze"}
          </button>
        </div>

        {/* Results Section */}
        <motion.div 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="bg-white p-6 rounded-lg shadow"
        >
          <h2 className="text-xl font-semibold mb-4">Analysis Results</h2>
          {result && (
            <div className="space-y-2">
              <p><span className="font-bold">SKU:</span> {result.detected_sku}</p>
              <p><span className="font-bold">Quantity:</span> {result.detected_qty}</p>
              <p><span className="font-bold">Damage:</span> {result.is_damaged ? "Yes" : "No"}</p>
              <p className="text-sm text-gray-600 italic mt-4">"{result.ai_explanation}"</p>
            </div>
          )}
        </motion.div>
      </div>
    </div>
  );
}