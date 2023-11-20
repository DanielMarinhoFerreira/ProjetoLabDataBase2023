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


// Inserções de administradores>
db.administradores.insertMany([
  {
      nome: "PLANNER CORRETORA DE VALORES SA",
      telefone: "1121722667",
      email: "inforegulatorio@planner.com.br",
      url_site: "www.planner.com.br",
      cnpj_admin: "00806535000154"
  },
  {
      nome: "RJI CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA",
      telefone: "213500450021",
      email: "backoffice.adm@rjicv.com.br",
      url_site: "www.rjicv.com.br",
      cnpj_admin: "42066258000130"
  },
  {
      nome: "BTG PACTUAL SERVIÇOS FINANCEIROS S/A DTVM",
      telefone: "1133833102",
      email: "ri.fundoslistados@btgpactual.com",
      url_site: "www.btgpactual.com",
      cnpj_admin: "59281253000123"
  },
  {
      nome: "OLIVEIRA TRUST DTVM S.A.",
      telefone: "2135140000",
      email: "ger2.fundos@oliveiratrust.com.br",
      url_site: "www.oliveiratrust.com.br",
      cnpj_admin: "36113876000191"
  }
]);

// Inserções de fundos>
db.fundos.insertMany([
  {
      ticker: 'AAZQ11',
      tipo_abbima: 'Tílos e Valores Mobiliarios',
      segmento: 'Indefinido',
      conta_emit: 24037284,
      num_cotas: 18095,
      razao_social: 'AZ QUEST SOLE FDO DE INV',
      cnpj: '44625826000111',
      nome_pregao: 'FIAGRO AAZQ',
      prazo_duracao: 'Indeterminado',
      tipo_gestao: 'ativa',
      cnpj_admin: '59281253000123'
  },
  {
      ticker: 'ABCP11',
      tipo_abbima: 'Renda',
      segmento: 'Shoppings',
      conta_emit: 4709082,
      num_cotas: 17747,
      razao_social: 'Grand Plaza Shopping',
      cnpj: '01201140000190',
      nome_pregao: 'Grand Plaza Shopping',
      prazo_duracao: 'Indeterminado',
      tipo_gestao: 'Passiva',
      cnpj_admin: '00806535000154'
  },
  {
      ticker: 'AFHI11',
      tipo_abbima: 'Tílos e Valores Mobiliarios',
      segmento: 'Papel',
      conta_emit: 3343095,
      num_cotas: 23891,
      razao_social: 'AF INVEST CRI',
      cnpj: '36642293000158',
      nome_pregao: 'FII AFHI CRI',
      prazo_duracao: 'Indeterminado',
      tipo_gestao: 'Ativa',
      cnpj_admin: '42066258000130'
  },
  {
      ticker: 'LVBI11',
      tipo_abbima: 'Renda',
      segmento: 'Imóveis Industriais e Logísticos',
      conta_emit: 1363338408,
      num_cotas: 11775177,
      razao_social: 'AF INVEST CRI',
      cnpj: '36642293000158',
      nome_pregao: 'FII VBI LOG',
      prazo_duracao: 'Indeterminado',
      tipo_gestao: 'Ativa',
      cnpj_admin: '59281253000123'
  },
  {
      ticker: 'SNCI11',
      tipo_abbima: 'Títulos e Valores Mobiliários',
      segmento: 'Indefinido',
      conta_emit: 413274896,
      num_cotas: 4200000,
      razao_social: 'SUNO RECEBÍVEIS IMOBILIÁRIOS FDO DE INV IMOB',
      cnpj: '41076710000182',
      nome_pregao: 'FII SUNO CRI',
      prazo_duracao: 'Indeterminado',
      tipo_gestao: 'Ativa',
      cnpj_admin: '59281253000123'
  },
  {
      ticker: 'AIEC11',
      tipo_abbima: 'Renda',
      segmento: 'Lajes Corporativas',
      conta_emit: 4824987,
      num_cotas: 15564,
      razao_social: 'AUTONOMY EDIF̓IOS CORPORATIVOS',
      cnpj: '35765826000126',
      nome_pregao: 'FII AUTONOMY',
      prazo_duracao: 'Indeterminado',
      tipo_gestao: 'Ativa',
      cnpj_admin: '36113876000191'
  }
]);

// Inserções de cotações>
db.cotacoes.insertMany([
  {
      ticker: 'AAZQ11',
      data_cota: '03/10/2023',
      cota_atual: 9.25,
      redimento_atual: 1.28,
      minimo_cota: 9.28,
      maximo_cota: 9.95,
      abertura: 9.29,
      volume_cotas: 24037284,
      mes: '04/10/2023',
      p_vp: 1.2
  },
  {
      ticker: 'ABCP11',
      data_cota: '03/10/2023',
      cota_atual: 66.81,
      redimento_atual: 0.89,
      minimo_cota: 63.47,
      maximo_cota: 109.7,
      abertura: 66.84,
      volume_cotas: 4709082,
      mes: '04/10/2023',
      p_vp: 1.0
  },
  {
      ticker: 'AFHI11',
      data_cota: '03/10/2023',
      cota_atual: 95.70,
      redimento_atual: 1.07,
      minimo_cota: 90.30,
      maximo_cota: 103.70,
      abertura: 95.98,
      volume_cotas: 3343095,
      mes: '04/10/2023',
      p_vp: 1.2
  },
  {
      ticker: 'AIEC11',
      data_cota: '03/10/2023',
      cota_atual: 63.16,
      redimento_atual: 1.16,
      minimo_cota: 60.52,
      maximo_cota: 70.86,
      abertura: 63.63,
      volume_cotas: 4824.987,
      mes: '04/10/2023',
      p_vp: 1.3
  },
  {
      ticker: 'AAZQ11',
      data_cota: '13/10/2023',
      cota_atual: 9.35,
      redimento_atual: 0.11,
      minimo_cota: 9.32,
      maximo_cota: 9.36,
      abertura: 9.34,
      volume_cotas: 24037284,
      mes: '13/10/2023',
      p_vp: 0.97
  },
  {
      ticker: 'ABCP11',
      data_cota: '13/10/2023',
      cota_atual: 67.80,
      redimento_atual: -0.31,
      minimo_cota: 67.68,
      maximo_cota: 68.01,
      abertura: 68.01,
      volume_cotas: 4709082,
      mes: '13/10/2023',
      p_vp: 0.74
  },
  {
      ticker: 'AFHI11',
      data_cota: '13/10/2023',
      cota_atual: 98.19,
      redimento_atual: 0.051,
      minimo_cota: 97.75,
      maximo_cota: 98.73,
      abertura: 98.14,
      volume_cotas: 3343095,
      mes: '13/10/2023',
      p_vp: 1.03
  },
  {
      ticker: 'AIEC11',
      data_cota: '13/10/2023',
      cota_atual: 62.40,
      redimento_atual: 0.22,
      minimo_cota: 62.40,
      maximo_cota: 63.10,
      abertura: 62.54,
      volume_cotas: 4824987,
      mes: '13/10/2023',
      p_vp: 0.66
  },
  {
      ticker: 'SNCI11',
      data_cota: '13/10/2023',
      cota_atual: 100.42,
      redimento_atual: 0.45,
      minimo_cota: 99.90,
      maximo_cota: 100.54,
      abertura: 99.97,
      volume_cotas: 4200000,
      mes: '13/10/2023',
      p_vp: 1.02
  },
  {
      ticker: 'LVBI11',
      data_cota: '13/10/2023',
      cota_atual: 118.04,
      redimento_atual: 0.068,
      minimo_cota: 117.03,
      maximo_cota: 118.07,
      abertura: 117.96,
      volume_cotas: 11775177,
      mes: '13/10/2023',
      p_vp: 1.02
  }
]);

// Inserções de dividendos>
db.dividendos.insertMany([
  {
      ticker: 'AAZQ11',
      data_pag: '05/11/2023',
      cota_base: 9.32,
      ult_divid: 1.28,
      rendimento: 0.12,
      div_yield: 12.47
  },
  {
      ticker: 'ABCP11',
      data_pag: '06/11/2023',
      cota_base: 66.95,
      ult_divid: 0.89,
      rendimento: 0.60,
      div_yield: 8.59
  },
  {
      ticker: 'AFHI11',
      data_pag: '05/11/2023',
      cota_base: 95.80,
      ult_divid: 1.07,
      rendimento: 1.05,
      div_yield: 13.03
  },
  {
      ticker: 'AIEC11',
      data_pag: '05/11/2023',
      cota_base: 63.31,
      ult_divid: 1.16,
      rendimento: 0.76,
      div_yield: 14.38
  },
  {
      ticker: 'AAZQ11',
      data_pag: '16/10/2023',
      cota_base: 9.40,
      ult_divid: 1.28,
      rendimento: 0.12,
      div_yield: 12.42
  },
  {
      ticker: 'ABCP11',
      data_pag: '06/10/2023',
      cota_base: 67.24,
      ult_divid: 0.89,
      rendimento: 0.60,
      div_yield: 8.45
  },
  {
      ticker: 'AFHI11',
      data_pag: '22/09/2023',
      cota_base: 98.23,
      ult_divid: 1.07,
      rendimento: 1.05,
      div_yield: 12.69
  },
  {
      ticker: 'AIEC11',
      data_pag: '09/10/2023',
      cota_base: 65.69,
      ult_divid: 1.16,
      rendimento: 0.76,
      div_yield: 14.57
  },
  {
      ticker: 'SNCI11',
      data_pag: '25/10/2023',
      cota_base: 100.48,
      ult_divid: 1.00,
      rendimento: 1.00,
      div_yield: 13.32
  },
  {
      ticker: 'LVBI11',
      data_pag: '06/10/2023',
      cota_base: 118.69,
      ult_divid: 0.67,
      rendimento: 0.79,
      div_yield: 7.75
  }
]);

db.FUNDOS.createIndex({ "CNPJ_ADMIN": 1 })
db.FUNDOS.updateMany({}, { $unset: { CNPJ_ADMIN: "" } })
db.FUNDOS.updateMany({}, { $set: { ADMINISTRADORES_CNPJ: 12345678901234 } })

db.COTACOES.createIndex({ "TICKER": 1 })
db.COTACOES.updateMany({}, { $unset: { TICKER: "" } })
db.COTACOES.updateMany({}, { $set: { FUNDOS_TICKER: "ABCDEF" } })

db.DIVIDENDOS.createIndex({ "TICKER": 1 })
db.DIVIDENDOS.updateMany({}, { $unset: { TICKER: "" } })
db.DIVIDENDOS.updateMany({}, { $set: { FUNDOS_TICKER: "ABCDEF" } })
