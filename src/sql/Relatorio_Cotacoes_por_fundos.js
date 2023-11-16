db.FUNDOS.find(
  {},
  {
    TICKER: 1,
    TIPO_ABBIMA: 1,
    SEGMENTO: 1,
    CONTA_EMIT: 1,
    NUM_COTAS: 1,
    RAZAO_SOCIAL: 1,
    CNPJ: 1,
    NOME_PREGAO: 1,
    PRAZO_DURACAO: 1,
    TIPO_GESTAO: 1,
    CNPJ_ADMIN: 1,
    _id: 0
  }
);