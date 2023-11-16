db.createCollection("ADMINISTRADORES")
db.ADMINISTRADORES.createIndex({ "CNPJ_ADMIN": 1 }, { unique: true })

db.createCollection("FUNDOS")
db.FUNDOS.createIndex({ "TICKER": 1 }, { unique: true })
db.FUNDOS.createIndex({ "CNPJ_ADMIN": 1 })
db.FUNDOS.createIndex({ "CNPJ": 1 })

db.createCollection("DIVIDENDOS")
db.DIVIDENDOS.createIndex({ "TICKER": 1 })

db.createCollection("COTACOES")
db.COTACOES.createIndex({ "TICKER": 1 })

db.ADMINISTRADORES.insert({
  CNPJ_ADMIN: 12345678901234,
  NOME: "Admin Name",
  TELEFONE: 123456789012,
  EMAIL: "admin@example.com",
  URL_SITE: "http://adminsite.com"
})

db.FUNDOS.insert({
  TICKER: "ABCDEF",
  TIPO_ABBIMA: "Type",
  SEGMENTO: "Segment",
  CONTA_EMIT: 12345678901234567890123456789012345678,
  NUM_COTAS: 12345678901234567890123456789012345678,
  RAZAO_SOCIAL: "Fund Name",
  CNPJ: 12345678901234,
  NOME_PREGAO: "Pregao",
  PRAZO_DURACAO: "Duration",
  TIPO_GESTAO: "Management",
  CNPJ_ADMIN: 12345678901234
})

db.DIVIDENDOS.insert({
  TICKER: "ABCDEF",
  DATA_PAG: "2023-01-01",
  COTA_BASE: 123.45,
  ULT_DIVID: 67.89,
  RENDIMENTO: 45.67,
  DIV_YIELD: 12.34
})

db.COTACOES.insert({
  TICKER: "ABCDEF",
  DATA_COTA: "2023-01-01",
  COTA_ATUAL: 123.45,
  RENDIMENTO_ATUAL: 45.67,
  MINIMO_COTA: 98.76,
  MAXIMO_COTA: 134.56,
  ABERTURA: 111.22,
  VOLUME_COTAS: 1234.5678,
  MES: "January",
  P_VP: 9.87
})

db.FUNDOS.createIndex({ "CNPJ_ADMIN": 1 })
db.FUNDOS.updateMany({}, { $unset: { CNPJ_ADMIN: "" } })
db.FUNDOS.updateMany({}, { $set: { ADMINISTRADORES_CNPJ: 12345678901234 } })

db.COTACOES.createIndex({ "TICKER": 1 })
db.COTACOES.updateMany({}, { $unset: { TICKER: "" } })
db.COTACOES.updateMany({}, { $set: { FUNDOS_TICKER: "ABCDEF" } })

db.DIVIDENDOS.createIndex({ "TICKER": 1 })
db.DIVIDENDOS.updateMany({}, { $unset: { TICKER: "" } })
db.DIVIDENDOS.updateMany({}, { $set: { FUNDOS_TICKER: "ABCDEF" } })
