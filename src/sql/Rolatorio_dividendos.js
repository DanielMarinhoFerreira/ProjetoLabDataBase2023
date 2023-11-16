db.DIVIDENDOS.aggregate([
  {
    $match: {
      "TICKER": { $ne: null }
    }
  },
  {
    $lookup: {
      from: "COTACOES",
      localField: "TICKER",
      foreignField: "TICKER",
      as: "cotacoes"
    }
  },
  {
    $unwind: "$cotacoes"
  },
  {
    $match: {
      "cotacoes.P_VP": { $ne: null }
    }
  },
  {
    $group: {
      _id: {
        TICKER: "$TICKER",
        P_VP: "$cotacoes.P_VP"
      },
      rendimento_total: { $sum: "$RENDIMENTO" }
    }
  },
  {
    $project: {
      _id: 0,
      TICKER: "$_id.TICKER",
      P_VP: "$_id.P_VP",
      rendimento_total: 1
    }
  }
]);
