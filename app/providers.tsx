/*
 * :file description: 
 * :name: /intelligent/app/providers.tsx
 * :author: 张德志
 * :copyright: (c) 2023, Tungee
 * :date created: 2023-12-04 20:40:44
 * :last editor: 张德志
 * :date last edited: 2023-12-04 20:55:25
 */
'use client'

import { NextUIProvider } from '@nextui-org/react'

export function Providers({ children }: { children: React.ReactNode }) {
  return (
    <NextUIProvider>
      {children}
    </NextUIProvider>
  )
}