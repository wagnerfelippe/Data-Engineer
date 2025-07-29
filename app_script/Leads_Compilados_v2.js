/**
* Copia todos os dados de uma aba em uma planilha para outra.
* Este script é otimizado para rodar via gatilhos automáticos (triggers),
* usando notificações por e-mail em vez de alertas na tela.
*/
function copiarDadosEntrePlanilhasEspecificas_v2() { // Renomeei para v2 para não confundir com a original
 // --- CONFIGURAÇÕES ---
 const idPlanilhaOrigem = "17agZWfnLmSSGxJYcdCHnQEfB6mWKH--viqw4RkN7zNo";
 const nomeAbaOrigem = "Compilado";
 const idPlanilhaDestino = "1saUdId_owBq2WaR3vquvGYUYJymdZd1wHfWtPhmNaBg";
 const nomeAbaDestino = "Compilado_Leads";

 try {
   // Pega o e-mail do usuário que autorizou o script para enviar notificações
   const emailNotificacao = Session.getActiveUser().getEmail();

   // 1. Abre as planilhas
   const planilhaOrigem = SpreadsheetApp.openById(idPlanilhaOrigem);
   const planilhaDestino = SpreadsheetApp.openById(idPlanilhaDestino);

   // 2. Obtém as abas
   const abaOrigem = planilhaOrigem.getSheetByName(nomeAbaOrigem);
   const abaDestino = planilhaDestino.getSheetByName(nomeAbaDestino);

   // 3. Validações (seu código de validação já era ótimo!)
   if (!abaOrigem) {
     throw new Error(`A aba '${nomeAbaOrigem}' não foi encontrada na Planilha de Origem.`);
   }
   if (!abaDestino) {
     throw new Error(`A aba '${nomeAbaDestino}' não foi encontrada na Planilha de Destino.`);
   }

   // 4. Obtém os dados da origem
   const dadosParaCopiar = abaOrigem.getDataRange().getValues();

   // 5. Limpa a aba de destino
   abaDestino.clearContents();

   // 6. Verifica e copia os dados
   if (dadosParaCopiar.length > 1 || (dadosParaCopiar.length === 1 && dadosParaCopiar[0].join("") !== "")) {
     // Copia os dados para o destino
     abaDestino.getRange(1, 1, dadosParaCopiar.length, dadosParaCopiar[0].length).setValues(dadosParaCopiar);
     
     // --- MUDANÇA 1: Notificação de Sucesso por E-mail ---
     const assunto = "✅ Sucesso: Automação de Leads Compilados";
     const corpo = `Os dados da aba '${nomeAbaOrigem}' foram copiados com sucesso para a aba '${nomeAbaDestino}'.\n\nTotal de linhas copiadas: ${dadosParaCopiar.length}.`;
     MailApp.sendEmail(emailNotificacao, assunto, corpo);
     Logger.log(corpo); // Também registra no log para depuração

   } else {
     // --- MUDANÇA 2: Notificação de Aba Vazia por E-mail ---
     const assunto = "⚠️ Atenção: Automação de Leads Compilados";
     const corpo = `A aba de origem '${nomeAbaOrigem}' está vazia. Nenhum dado foi copiado.`;
     MailApp.sendEmail(emailNotificacao, assunto, corpo);
     Logger.log(corpo);
   }

 } catch (e) {
   // --- MUDANÇA 3: Notificação de ERRO por E-mail ---
   // Esta é a mudança mais importante. Agora você será notificado se a automação falhar.
   const emailNotificacaoErro = Session.getActiveUser().getEmail();
   const assuntoErro = "❌ ERRO: Falha na Automação de Leads Compilados";
   const corpoErro = `Ocorreu um erro ao tentar executar a automação:\n\n${e.message}\n\nStack Trace:\n${e.stack}`;
   
   MailApp.sendEmail(emailNotificacaoErro, assuntoErro, corpoErro);
   console.error(e); // Mantém o erro no log do Apps Script para análise detalhada
 }
}