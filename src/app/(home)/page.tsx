'use client'

import { useAuth } from '@/src/context/AuthContext'
import React from 'react'

const page = () => {
  const { user } = useAuth();

  return (
    <div className='p-8 bg-slate-200 w-full h-full'>
      <h1 className='text-2xl font-bold mb-8'>Hello from dashboard</h1> 
      <button className='bg-blue-500 p-2 rounded-md' onClick={() => alert(user?.role)}>Click here</button>
    </div>
  )
}

export default page
