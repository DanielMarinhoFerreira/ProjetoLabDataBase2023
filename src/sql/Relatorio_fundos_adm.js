db.FUNDOS.aggregate([
  {
    $lookup: {
      from: "ADMINISTRADORES",
      localField: "CNPJ_ADMIN",
      foreignField: "CNPJ_ADMIN",
      as: "administrador"
    }
  },
  {
    $unwind: "$administrador"
  },
  {
    $match: {
      TICKER: { $ne: null }
    }
  },
  {
    $sort: {
      TICKER: 1
    }
  },
  {
    $project: {
      _id: 0,
      TICKER: "$TICKER",
      TIPO_ABBIMA: "$TIPO_ABBIMA",
      SEGMENTO: "$SEGMENTO",
      CNPJ_ADMIN: "$administrador.CNPJ_ADMIN",
      NOME_ADMIN: "$administrador.NOME"
    }
  }
]);
