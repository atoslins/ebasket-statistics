import type React from "react"
import type { Metadata } from "next"
import { Inter } from "next/font/google"
import "./globals.css"

const inter = Inter({ subsets: ["latin"] })

export const metadata: Metadata = {
  title: "Estatísticas eBasket",
  description: "Sistema de histórico de confrontos de basquete",
    generator: 'v0.dev'
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <div className="min-h-screen flex flex-col">
          <header className="bg-gradient-to-r from-orange-600 to-orange-500 text-white py-4 shadow-md">
            <div className="container mx-auto px-4">
              <h1 className="text-2xl font-bold">Estatísticas eBasket</h1>
            </div>
          </header>
          <main className="flex-grow container mx-auto px-4 py-8">{children}</main>
          <footer className="bg-gray-100 py-4 border-t">
            <div className="container mx-auto px-4 text-center text-gray-600">
              <p>Sistema de Histórico de Confrontos &copy; {new Date().getFullYear()}</p>
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}



import './globals.css'