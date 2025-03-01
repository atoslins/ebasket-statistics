"use client"

import { useSearchParams } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { ArrowLeft, ShoppingBasketIcon as Basketball, Calendar, Trophy } from "lucide-react"
import Link from "next/link"
import { MatchTable } from "@/components/match-table"
import { StatsCards } from "@/components/stats-cards"
import { PlayerComparison } from "@/components/player-comparison"

// Mock data for demonstration
const mockMatches = [
  {
    id: 1,
    formatted_date: "10/01/2023",
    hora: "19:30",
    time1_placar_periodos: "25-20, 22-18, 19-24, 28-22",
    time1_nome: "Lakers",
    time1_jogador: "LeBron James",
    time1_placar_final: 94,
    time2_nome: "Warriors",
    time2_jogador: "Stephen Curry",
    time2_placar_final: 84,
    time2_placar_periodos: "20-25, 18-22, 24-19, 22-28",
  },
  {
    id: 2,
    formatted_date: "15/02/2023",
    hora: "20:00",
    time1_placar_periodos: "22-24, 26-20, 30-28, 25-22",
    time1_nome: "Warriors",
    time1_jogador: "Stephen Curry",
    time1_placar_final: 103,
    time2_nome: "Lakers",
    time2_jogador: "LeBron James",
    time2_placar_final: 94,
    time2_placar_periodos: "24-22, 20-26, 28-30, 22-25",
  },
  {
    id: 3,
    formatted_date: "05/03/2023",
    hora: "18:45",
    time1_placar_periodos: "28-22, 24-26, 19-18, 30-28",
    time1_nome: "Lakers",
    time1_jogador: "LeBron James",
    time1_placar_final: 101,
    time2_nome: "Warriors",
    time2_jogador: "Stephen Curry",
    time2_placar_final: 94,
    time2_placar_periodos: "22-28, 26-24, 18-19, 28-30",
  },
  {
    id: 4,
    formatted_date: "12/04/2023",
    hora: "21:15",
    time1_placar_periodos: "25-27, 30-22, 28-25, 22-24",
    time1_nome: "Warriors",
    time1_jogador: "Stephen Curry",
    time1_placar_final: 105,
    time2_nome: "Lakers",
    time2_jogador: "LeBron James",
    time2_placar_final: 98,
    time2_placar_periodos: "27-25, 22-30, 25-28, 24-22",
  },
]

export default function Confrontos() {
  const searchParams = useSearchParams()
  const player1 = searchParams.get("player1") || ""
  const player2 = searchParams.get("player2") || ""

  // In a real app, you would fetch this data based on the players
  const matches = player1 && player2 ? mockMatches : []

  // Calculate stats
  const totalMatches = matches.length
  const player1Wins = matches.filter(
    (match) =>
      (match.time1_jogador === player1 && match.time1_placar_final > match.time2_placar_final) ||
      (match.time2_jogador === player1 && match.time2_placar_final > match.time1_placar_final),
  ).length
  const player2Wins = matches.filter(
    (match) =>
      (match.time1_jogador === player2 && match.time1_placar_final > match.time2_placar_final) ||
      (match.time2_jogador === player2 && match.time2_placar_final > match.time1_placar_final),
  ).length

  return (
    <div className="animate-in">
      <Button variant="outline" asChild className="mb-6">
        <Link href="/">
          <ArrowLeft className="mr-2 h-4 w-4" />
          Voltar
        </Link>
      </Button>

      {player1 && player2 ? (
        <>
          <Card className="shadow-lg mb-8">
            <CardHeader className="bg-gradient-to-r from-orange-600 to-orange-500 text-white rounded-t-lg">
              <CardTitle className="flex items-center">
                <Basketball className="mr-2 h-5 w-5" />
                Confrontos: {player1} vs {player2}
              </CardTitle>
              <CardDescription className="text-orange-100">
                Histórico completo de partidas entre os jogadores
              </CardDescription>
            </CardHeader>
            <CardContent className="pt-6">
              {matches.length > 0 ? (
                <>
                  <StatsCards
                    player1={player1}
                    player2={player2}
                    totalMatches={totalMatches}
                    player1Wins={player1Wins}
                    player2Wins={player2Wins}
                  />

                  <PlayerComparison
                    player1={player1}
                    player2={player2}
                    player1Wins={player1Wins}
                    player2Wins={player2Wins}
                    totalMatches={totalMatches}
                  />

                  <div className="mt-8">
                    <h3 className="text-lg font-semibold mb-4">Detalhes dos Confrontos</h3>
                    <MatchTable matches={matches} player1={player1} player2={player2} />
                  </div>
                </>
              ) : (
                <div className="bg-blue-50 text-blue-700 p-4 rounded-lg flex items-center">
                  <Calendar className="h-5 w-5 mr-2" />
                  <p>
                    Nenhum confronto encontrado entre {player1} e {player2}.
                  </p>
                </div>
              )}
            </CardContent>
          </Card>
        </>
      ) : (
        <Card className="shadow-lg">
          <CardContent className="pt-6">
            <div className="bg-amber-50 text-amber-700 p-4 rounded-lg flex items-center">
              <Trophy className="h-5 w-5 mr-2" />
              <p>Selecione dois jogadores para ver o histórico de confrontos.</p>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  )
}

