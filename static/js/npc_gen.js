function fetchFullNpcDetails() {
    const npcCount = document.getElementById('npcCount').value || 15;
    fetch(`/npcs_generator_temp?number=${npcCount}`)
        .then(response => response.json())
        .then(data => {
            const npcFullListElement = document.getElementById('npc-full-list');
            npcFullListElement.innerHTML = ''; // Clear previous content

            if (data.npcs_temp && data.npcs_temp.npc && Object.keys(data.npcs_temp.npc).length > 0) {
                Object.keys(data.npcs_temp.npc).forEach(npcName => {
                    const npcData = data.npcs_temp.npc[npcName];
                    const npcDetailDiv = document.createElement('div');
                    npcDetailDiv.classList.add('npc-detail');

                    const visibleContentDiv = document.createElement('div');
                    visibleContentDiv.innerHTML = `
                        <h3>${npcName}</h3>
                        <p><strong>Race:</strong> ${npcData.race}</p>
                        <p><strong>Subrace:</strong> ${npcData.subrace || "None"}</p>
                        <p><strong>Class:</strong> ${npcData.class}</p>
                    `;
                    npcDetailDiv.appendChild(visibleContentDiv);

                    const collapsibleContent = document.createElement('div');
                    collapsibleContent.classList.add('collapsible-content');
                    collapsibleContent.style.maxHeight = '0'; // Initially hidden
                    
                    // Level
                    const levelInfo = document.createElement('p');
                    levelInfo.innerHTML = `<strong>Level:</strong> ${npcData.level}`;
                    collapsibleContent.appendChild(levelInfo);

                    // HP
                    const hpInfo = document.createElement('p');
                    hpInfo.innerHTML = `<strong>HP:</strong> ${npcData.hp}`;
                    collapsibleContent.appendChild(hpInfo);

                    // General Race Info
                    const generalRaceInfo = document.createElement('p');
                    generalRaceInfo.innerHTML = `<strong>General Race Info:</strong> ${npcData.special_race_info}`;
                    collapsibleContent.appendChild(generalRaceInfo);

                    levelInfo.setAttribute('id', 'card-element')
                    hpInfo.setAttribute('id', 'card-element')

                    // Stat Block
                    const statBlockDiv = document.createElement('div');
                    const statBlockHeader = document.createElement('h4');
                    statBlockHeader.textContent = 'Stat Block:';
                    statBlockDiv.appendChild(statBlockHeader);
                    Object.entries(npcData.stat_block).forEach(([statName, value]) => {
                        const statItem = document.createElement('p');
                        statItem.innerHTML = `<strong>${statName}:</strong> ${value}`;
                        statBlockDiv.appendChild(statItem);
                    });
                    collapsibleContent.appendChild(statBlockDiv);

                    // Starting Pack
                    const packDiv = document.createElement('div');
                    const packHeader = document.createElement('h4');
                    packHeader.textContent = 'Gear & Equipment:';
                    packDiv.appendChild(packHeader);
                    const packList = document.createElement('ul');
                    npcData.starting_pack.forEach(item => {
                        const itemLi = document.createElement('li');
                        itemLi.textContent = item;
                        packList.appendChild(itemLi);
                    });
                    packDiv.appendChild(packList);
                    collapsibleContent.appendChild(packDiv);

                    npcDetailDiv.appendChild(collapsibleContent);
                    visibleContentDiv.addEventListener('click', function() {
                        const isCollapsed = collapsibleContent.style.maxHeight === '' || collapsibleContent.style.maxHeight === '0px';
                        collapsibleContent.style.maxHeight = isCollapsed ? `${collapsibleContent.scrollHeight}px` : '0';
                    });

                    npcFullListElement.appendChild(npcDetailDiv);
                });
            } else {
                npcFullListElement.textContent = 'No NPC details found.';
            }
        })
        .catch(error => {
            console.error('Error fetching NPC details:', error);
            npcFullListElement.textContent = 'Failed to load NPC details.';
        });
}

document.getElementById('toggleAll').addEventListener('click', function() {
    const allCollapsibleContent = document.querySelectorAll('.collapsible-content');
    let isAnyExpanded = Array.from(allCollapsibleContent).some(content => content.style.maxHeight !== '' && content.style.maxHeight !== '0px');
    
    allCollapsibleContent.forEach(content => {
        if (isAnyExpanded) {
            content.style.maxHeight = '0';
        } else {
            setTimeout(() => content.style.maxHeight = content.scrollHeight + 'px', 10);
        }
    });
});
