"use client"

import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Calendar, Clock } from "lucide-react"
import { useState } from "react"
import { Button } from "./ui/button"
import { Card } from "./ui/card"

interface Match {
  id: number
  formatted_date: string
  hora: string
  time1_placar_periodos: string
  time1_nome: string
  time1_jogador: string
  time1_placar_final: number
  time2_nome: string
  time2_jogador: string
  time2_placar_final: number
  time2_placar_periodos: string
}

interface MatchTableProps {
  matches: Match[]
  player1: string
  player2: string
}

export function MatchTable({ matches, player1, player2 }: MatchTableProps) {
  const [expandedMatch, setExpandedMatch] = useState<number | null>(null)

  const toggleExpand = (id: number) => {
    setExpandedMatch(expandedMatch === id ? null : id)
  }

  return (
    <div className="overflow-x-auto">
      <Table className="border rounded-lg">
        <TableHeader className="bg-gray-50">
          <TableRow>
            <TableHead className="w-[100px]">Data</TableHead>
            <TableHead>Time</TableHead>
            <TableHead>Jogador</TableHead>
            <TableHead className="text-center">Placar</TableHead>
            <TableHead>Time</TableHead>
            <TableHead>Jogador</TableHead>
            <TableHead className="text-right">Detalhes</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {matches.map((match) => {
            const team1Winner = match.time1_placar_final > match.time2_placar_final
            const team2Winner = match.time2_placar_final > match.time1_placar_final

            return (
              <>
                <TableRow key={match.id} className="hover:bg-gray-50">
                  <TableCell className="font-medium">
                    <div className="flex items-center">
                      <Calendar className="h-4 w-4 mr-1 text-gray-500" />
                      {match.formatted_date}
                    </div>
                    <div className="text-xs text-gray-500 flex items-center mt-1">
                      <Clock className="h-3 w-3 mr-1" />
                      {match.hora}
                    </div>
                  </TableCell>
                  <TableCell>
                    <div className="font-medium">{match.time1_nome}</div>
                  </TableCell>
                  <TableCell>
                    <div
                      className={
                        match.time1_jogador === player1
                          ? "player-highlight-1"
                          : match.time1_jogador === player2
                            ? "player-highlight-2"
                            : ""
                      }
                    >
                      {match.time1_jogador}
                    </div>
                  </TableCell>
                  <TableCell>
                    <div className="flex items-center justify-center space-x-2">
                      <span className={`score-badge ${team1Winner ? "winner" : "loser"}`}>
                        {match.time1_placar_final}
                      </span>
                      <span className="text-gray-500">x</span>
                      <span className={`score-badge ${team2Winner ? "winner" : "loser"}`}>
                        {match.time2_placar_final}
                      </span>
                    </div>
                  </TableCell>
                  <TableCell>
                    <div className="font-medium">{match.time2_nome}</div>
                  </TableCell>
                  <TableCell>
                    <div
                      className={
                        match.time2_jogador === player1
                          ? "player-highlight-1"
                          : match.time2_jogador === player2
                            ? "player-highlight-2"
                            : ""
                      }
                    >
                      {match.time2_jogador}
                    </div>
                  </TableCell>
                  <TableCell className="text-right">
                    <Button variant="ghost" size="sm" onClick={() => toggleExpand(match.id)}>
                      {expandedMatch === match.id ? "Ocultar" : "Ver períodos"}
                    </Button>
                  </TableCell>
                </TableRow>
                {expandedMatch === match.id && (
                  <TableRow>
                    <TableCell colSpan={7} className="p-0">
                      <Card className="m-2 bg-gray-50 border-gray-200">
                        <div className="p-4">
                          <h4 className="font-medium mb-2">Placar por Períodos</h4>
                          <div className="grid grid-cols-2 gap-4">
                            <div>
                              <p className="text-sm font-medium">{match.time1_nome}</p>
                              <p className="text-sm">{match.time1_placar_periodos}</p>
                            </div>
                            <div>
                              <p className="text-sm font-medium">{match.time2_nome}</p>
                              <p className="text-sm">{match.time2_placar_periodos}</p>
                            </div>
                          </div>
                        </div>
                      </Card>
                    </TableCell>
                  </TableRow>
                )}
              </>
            )
          })}
        </TableBody>
      </Table>
    </div>
  )
}

