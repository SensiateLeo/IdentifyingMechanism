window.mutations_observed = []
window.tipos_mutacoes = []

window.observer = new MutationObserver(function(mutations) {
     mutations.forEach(function(mutation) {
        var target = mutation.target;
        var type = mutation.type
        window.mutations_observed.push(mutation);
        window.tipos_mutacoes.push(target);
        if (mutation.addedNodes) {
            for (var i = 0; i < mutation.addedNodes.length; i++) {
                if (mutation.addedNodes[i].nodeType === 1)
                    window.mutations_observed.push(mutation.addedNodes[i]);
                    window.tipos_mutacoes.push(mutation.addedNodes[i]);
            };
        }
        console.log(mutation.type);
        console.log(mutation.target)
        console.log(mutation.attributes)
        console.log(mutation.addedNodes);
    });
});

observer.observe(document.body, {
    attributes: true,
    childList: true,
    subtree: true,
    characterData: true
});
