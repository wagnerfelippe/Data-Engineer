function copiarDadosEntrePlanilhasEspecificas() {
// --- CONFIGURAÇÕES ---
// 1. Informações da Planilha de Origem (Planilha X)
const idPlanilhaOrigem = "17agZWfnLmSSGxJYcdCHnQEfB6mWKH--viqw4RkN7zNo"; // <<< SUBSTITUA PELO ID DA PLANILHA X
const nomeAbaOrigem = "Compilado"; // Nome da aba na Planilha X

// 2. Informações da Planilha de Destino (Planilha Y)
const idPlanilhaDestino = "1saUdId_owBq2WaR3vquvGYUYJymdZd1wHfWtPhmNaBg"; // <<< SUBSTITUA PELO ID DA PLANILHA Y
const nomeAbaDestino = "Compilado_Leads"; // Nome da aba na Planilha Y

// DICA: Para encontrar o ID de uma planilha, abra-a no navegador.
// O ID é a parte da URL entre "/d/" e "/edit", por exemplo:
// https://docs.google.com/spreadsheets/d/123ABC_XYZ/edit#gid=0
// O ID seria: 123ABC_XYZ

// --- EXECUÇÃO ---
try {
  // 1. Abre as planilhas de origem e destino
  const planilhaOrigem = SpreadsheetApp.openById(idPlanilhaOrigem);
  const planilhaDestino = SpreadsheetApp.openById(idPlanilhaDestino);

  // 2. Obtém as abas específicas
  const abaOrigem = planilhaOrigem.getSheetByName(nomeAbaOrigem);
  const abaDestino = planilhaDestino.getSheetByName(nomeAbaDestino);

  // 3. Valida se as abas e planilhas foram encontradas
  if (!planilhaOrigem) {
    throw new Error(`Erro: Planilha de origem com ID '${idPlanilhaOrigem}' não encontrada. Verifique o ID.`);
  }
  if (!abaOrigem) {
    throw new Error(`Erro: A aba '${nomeAbaOrigem}' não foi encontrada na Planilha de Origem. Verifique o nome da aba.`);
  }
  if (!planilhaDestino) {
    throw new Error(`Erro: Planilha de destino com ID '${idPlanilhaDestino}' não encontrada. Verifique o ID.`);
  }
  if (!abaDestino) {
    throw new Error(`Erro: A aba '${nomeAbaDestino}' não foi encontrada na Planilha de Destino. Verifique o nome da aba.`);
  }

  // 4. Obtém todos os dados da aba de origem
  // getDataRange() pega o intervalo que contém todos os dados.
  const dadosParaCopiar = abaOrigem.getDataRange().getValues();

  // 5. Limpa o conteúdo da aba de destino antes de colar os novos dados
  // Isso garante que não fiquem dados antigos ou duplicados.
  abaDestino.clearContents(); // Limpa apenas os valores, mantendo formatação existente

  // 6. Verifica se há dados para copiar e os define na aba de destino
  if (dadosParaCopiar.length > 0) {
    // Define o intervalo na aba de destino com base no tamanho dos dados
    // Começa na célula A1 (linha 1, coluna 1)
    abaDestino.getRange(1, 1, dadosParaCopiar.length, dadosParaCopiar[0].length).setValues(dadosParaCopiar);
    SpreadsheetApp.getUi().alert(`Sucesso! Dados da aba '${nomeAbaOrigem}' (Planilha X) copiados para a aba '${nomeAbaDestino}' (Planilha Y).`);
  } else {
    SpreadsheetApp.getUi().alert(`Atenção: A aba '${nomeAbaOrigem}' (Planilha X) está vazia. Nada foi copiado.`);
  }

} catch (e) {
  // Captura e exibe qualquer erro que ocorra durante a execução
  SpreadsheetApp.getUi().alert(`Ocorreu um erro: ${e.message}`);
  console.error(e); // Para depuração, o erro completo aparecerá nos logs do Apps Script
}
}
