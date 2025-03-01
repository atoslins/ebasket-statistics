import { Card, CardContent } from "@/components/ui/card"
import { Progress } from "@/components/ui/progress"

interface PlayerComparisonProps {
  player1: string
  player2: string
  player1Wins: number
  player2Wins: number
  totalMatches: number
}

export function PlayerComparison({ player1, player2, player1Wins, player2Wins, totalMatches }: PlayerComparisonProps) {
  const player1Percentage = totalMatches > 0 ? Math.round((player1Wins / totalMatches) * 100) : 0
  const player2Percentage = totalMatches > 0 ? Math.round((player2Wins / totalMatches) * 100) : 0

  return (
    <Card className="mt-8">
      <CardContent className="pt-6">
        <h3 className="text-lg font-semibold mb-4">Comparação de Desempenho</h3>

        <div className="space-y-6">
          <div className="space-y-2">
            <div className="flex justify-between">
              <div className="player-highlight-1">{player1}</div>
              <div>
                {player1Wins} vitória{player1Wins !== 1 ? "s" : ""} ({player1Percentage}%)
              </div>
            </div>
            <Progress value={player1Percentage} className="h-2 bg-gray-200" indicatorClassName="bg-orange-500" />
          </div>

          <div className="space-y-2">
            <div className="flex justify-between">
              <div className="player-highlight-2">{player2}</div>
              <div>
                {player2Wins} vitória{player2Wins !== 1 ? "s" : ""} ({player2Percentage}%)
              </div>
            </div>
            <Progress value={player2Percentage} className="h-2 bg-gray-200" indicatorClassName="bg-blue-500" />
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

