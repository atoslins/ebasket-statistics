"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { ArrowRight, ShoppingBasketIcon as Basketball } from "lucide-react"
import Link from "next/link"

// Mock data for demonstration
const mockPlayers = [
  "LeBron James",
  "Stephen Curry",
  "Kevin Durant",
  "Giannis Antetokounmpo",
  "Luka Dončić",
  "Nikola Jokić",
  "Joel Embiid",
  "Jayson Tatum",
  "Damian Lillard",
  "Anthony Davis",
]

export default function Home() {
  const [player1, setPlayer1] = useState<string>("")
  const [player2, setPlayer2] = useState<string>("")
  const [opponents, setOpponents] = useState<string[]>([])

  // Simulate fetching opponents when player1 is selected
  const handlePlayer1Change = (value: string) => {
    setPlayer1(value)
    setPlayer2("")

    // In a real app, this would be an API call
    // For demo, filter out the selected player from the list
    const mockOpponents = mockPlayers.filter((player) => player !== value)
    setOpponents(mockOpponents)
  }

  return (
    <div className="max-w-2xl mx-auto animate-in">
      <Button variant="outline" asChild className="mb-6">
        <Link href="/">
          <ArrowRight className="mr-2 h-4 w-4 rotate-180" />
          Voltar
        </Link>
      </Button>

      <Card className="shadow-lg">
        <CardHeader className="bg-gradient-to-r from-orange-600 to-orange-500 text-white rounded-t-lg">
          <CardTitle className="flex items-center">
            <Basketball className="mr-2 h-5 w-5" />
            Selecione os Jogadores
          </CardTitle>
          <CardDescription className="text-orange-100">
            Escolha dois jogadores para ver o histórico de confrontos
          </CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <form className="space-y-6">
            <div className="space-y-2">
              <label htmlFor="player1" className="text-sm font-medium">
                Jogador 1
              </label>
              <Select value={player1} onValueChange={handlePlayer1Change}>
                <SelectTrigger id="player1">
                  <SelectValue placeholder="Selecione um jogador" />
                </SelectTrigger>
                <SelectContent>
                  {mockPlayers.map((player) => (
                    <SelectItem key={player} value={player}>
                      {player}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <label htmlFor="player2" className="text-sm font-medium">
                Jogador 2
              </label>
              <Select value={player2} onValueChange={setPlayer2} disabled={!player1 || opponents.length === 0}>
                <SelectTrigger id="player2">
                  <SelectValue
                    placeholder={
                      !player1
                        ? "Selecione o jogador 1 primeiro"
                        : opponents.length === 0
                          ? "Nenhum adversário encontrado"
                          : "Selecione um jogador"
                    }
                  />
                </SelectTrigger>
                <SelectContent>
                  {opponents.map((player) => (
                    <SelectItem key={player} value={player}>
                      {player}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <Button className="w-full" disabled={!player1 || !player2} asChild>
              <Link href={`/confrontos?player1=${encodeURIComponent(player1)}&player2=${encodeURIComponent(player2)}`}>
                Ver Histórico de Confrontos
              </Link>
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}

