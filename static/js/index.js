function fetchNpcNames() {
    fetch('/npc_names')
    .then(response => response.json())
    .then(data => {
        const npcNamesList = document.getElementById('npc-names-list');
        if (data.npc_names && data.npc_names.length > 0) {
        const list = document.createElement('ul');
        data.npc_names.forEach(name => {
            const item = document.createElement('li');
            item.textContent = name;
            list.appendChild(item);
        });
        npcNamesList.appendChild(list);
        } else {
        npcNamesList.textContent = 'No NPC names found.';
        }
    })
    .catch(error => {
        console.error('Error fetching NPC names:', error);
        document.getElementById('npc-names-list').textContent = 'Failed to load NPC names.';
    });
}

function fetchTempNpcNames() {
    fetch('/npcs_generator_temp?number=5')
    .then(response => response.json())
    .then(data => {
        const npcNamesListElement = document.getElementById('npc-names-list');
        npcNamesListElement.innerHTML = ''; // Clear previous content

        // Correct the path according to your API response
        if (data.npcs_temp && data.npcs_temp.npc && Object.keys(data.npcs_temp.npc).length > 0) {
            const list = document.createElement('ul');
            
            // Iterate over the NPC names correctly
            Object.keys(data.npcs_temp.npc).forEach(npcName => {
                const item = document.createElement('li');
                item.textContent = npcName; // Display the NPC name
                list.appendChild(item);
            });
            npcNamesListElement.appendChild(list);
        } else {
            npcNamesListElement.textContent = 'No NPC names found.';
        }
    })
    .catch(error => {
        console.error('Error fetching NPC names:', error);
        npcNamesListElement.textContent = 'Failed to load NPC names.';
    });
}

function fetchFullNpcDetails() {
    fetch('/npcs_generator_temp?number=5')
        .then(response => response.json())
        .then(data => {
            const npcFullListElement = document.getElementById('npc-full-list');
            npcFullListElement.innerHTML = ''; // Clear previous content

            if (data.npcs_temp && data.npcs_temp.npc && Object.keys(data.npcs_temp.npc).length > 0) {
                Object.keys(data.npcs_temp.npc).forEach(npcName => {
                    const npcData = data.npcs_temp.npc[npcName];

                    // Create a container for each NPC's details
                    const npcDetailDiv = document.createElement('div');
                    npcDetailDiv.classList.add('npc-detail'); // For styling purposes

                    // NPC Name
                    const nameHeader = document.createElement('h3');
                    nameHeader.textContent = npcName;
                    npcDetailDiv.appendChild(nameHeader);

                    // NPC properties excluding the starting pack and stat block
                    Object.keys(npcData).forEach(key => {
                        if (key !== "starting_pack" && key !== "stat_block") {
                            const detailParagraph = document.createElement('p');
                            detailParagraph.textContent = `${key}: ${npcData[key]}`;
                            npcDetailDiv.appendChild(detailParagraph);
                        }
                    });

                    // NPC Stat Block
                    const statBlockHeader = document.createElement('h4');
                    statBlockHeader.textContent = 'Stat Block:';
                    npcDetailDiv.appendChild(statBlockHeader);
                    const statBlockDiv = document.createElement('div'); // Changed to div for inline display
                    statBlockDiv.className = 'stat-block';
                    Object.entries(npcData.stat_block).forEach(([statName, value]) => {
                        const statItem = document.createElement('div'); // Changed to div for each stat
                        statItem.textContent = `${statName}: ${value}`;
                        statBlockDiv.appendChild(statItem);
                    });
                    npcDetailDiv.appendChild(statBlockDiv);

                    // NPC Starting Pack (array handling)
                    const packHeader = document.createElement('h4');
                    packHeader.textContent = 'Starting Pack:';
                    npcDetailDiv.appendChild(packHeader);
                    const packList = document.createElement('ul');
                    npcData.starting_pack.forEach(item => {
                        const itemLi = document.createElement('li');
                        itemLi.textContent = item;
                        packList.appendChild(itemLi);
                    });
                    npcDetailDiv.appendChild(packList);

                    // Append this NPC's details to the main list container
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

