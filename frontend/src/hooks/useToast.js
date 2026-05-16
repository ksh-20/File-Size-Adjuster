import toast from 'react-hot-toast'

export const useToast = () => {
  const success = (message) => {
    toast.success(message)
  }

  const error = (message) => {
    toast.error(message)
  }

  return {
    success,
    error
  }
}