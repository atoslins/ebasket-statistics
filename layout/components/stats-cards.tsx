import { Card, CardContent } from "@/components/ui/card"
import { Trophy, Calendar } from "lucide-react"

interface StatsCardsProps {
  player1: string
  player2: string
  totalMatches: number
  player1Wins: number
  player2Wins: number
}

export function StatsCards({ player1, player2, totalMatches, player1Wins, player2Wins }: StatsCardsProps) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
      <Card>
        <CardContent className="pt-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-500">Total de Confrontos</p>
              <p className="text-3xl font-bold">{totalMatches}</p>
            </div>
            <div className="h-12 w-12 rounded-full bg-orange-100 flex items-center justify-center text-orange-600">
              <Calendar className="h-6 w-6" />
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="pt-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-500">Vitórias de {player1}</p>
              <p className="text-3xl font-bold">{player1Wins}</p>
            </div>
            <div className="h-12 w-12 rounded-full bg-blue-100 flex items-center justify-center text-blue-600">
              <Trophy className="h-6 w-6" />
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardContent className="pt-6">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-500">Vitórias de {player2}</p>
              <p className="text-3xl font-bold">{player2Wins}</p>
            </div>
            <div className="h-12 w-12 rounded-full bg-green-100 flex items-center justify-center text-green-600">
              <Trophy className="h-6 w-6" />
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

