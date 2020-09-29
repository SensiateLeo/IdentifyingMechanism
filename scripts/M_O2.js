var target = document.getElementById('ui-datepicker-div');

window.observer = new MutationObserver(function(mutations) {
    var i = 0;
    mutations.forEach(function(mutation) {
        //console.log(mutation.type);
        //console.log(mutation.attributes)
        //console.log(mutation.attributeOldValue)
        //i = i + 1;

        //Para apresentação "resumida" das alterações
        if (mutation.type === 'childList') {
            for (var i = 0; i < mutation.addedNodes.length; i++) {
            console.log('  "' + mutation.addedNodes[i].textContent + '" adicionado');
          }
          for (var i = 0; i < mutation.removedNodes.length; i++) {
            console.log('  "' + mutation.removedNodes[i].textContent + '" removido');
          }
        } else {
            console.log('  "' + mutation.attributeName + '" alterado')
        }

        //Para apresentação completa das alterações - atributos, valores, etc...
        if (mutation.type === 'childList') {
            console.log("\n")
            for (var i = 0; i < mutation.addedNodes.length; i++) {
            console.log('  "' + mutation.addedNodes[i].textContent + '" adicionado');
          }
          for (var i = 0; i < mutation.removedNodes.length; i++) {
            console.log('  "' + mutation.removedNodes[i].textContent + '" removido');
          }
          console.log("\n")
        } else {
           console.log('Valor  "' + mutation.attributeName + '" alterado - Valor anterior: ' + mutation.oldValue + '\n')
        }
    });
    //console.log(i);
});

var config = {
              attributes: true,
              attributeOldValue: true,
              characterData: true,
              characterDataOldValue: true,
              childList: true,
              subtree: true}

window.observer.observe(target, config);