import { Toaster } from 'react-hot-toast'

export default function Toast() {
  return (
    <Toaster
      position="top-right"
      toastOptions={{
        duration: 3000,
        style: {
          background: '#171722',
          color: '#fff',
          border: '1px solid rgba(255,255,255,0.1)'
        }
      }}
    />
  )
}