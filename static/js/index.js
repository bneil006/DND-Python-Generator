document.addEventListener('DOMContentLoaded', () => {
    // Function to fetch and display NPC details
    function fetchFullNpcDetails() {
        const npcCount = document.getElementById('npcCount').value || 15;
        fetch(`/gen_npc?number=${npcCount}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const npcFullListElement = document.getElementById('npc-full-list');
                npcFullListElement.innerHTML = ''; // Clear previous content

                if (data.npcs_temp && data.npcs_temp.npcs && data.npcs_temp.npcs.length > 0) {
                    data.npcs_temp.npcs.forEach(npcData => {
                        const npcDetailDiv = document.createElement('div');
                        npcDetailDiv.classList.add('npc-detail');

                        const visibleContentDiv = document.createElement('div');
                        visibleContentDiv.innerHTML = `
                            <h3>${npcData.name}</h3>
                            <p><strong>Race:</strong> ${npcData.race}</p>
                            <p><strong>Subrace:</strong> ${npcData.subrace || "None"}</p>
                            <p><strong>Class:</strong> ${npcData.class}</p>
                        `;
                        npcDetailDiv.appendChild(visibleContentDiv);

                        const collapsibleContent = document.createElement('div');
                        collapsibleContent.classList.add('collapsible-content');
                        collapsibleContent.style.maxHeight = '0'; // Initially hidden

                        const levelInfo = document.createElement('p');
                        levelInfo.innerHTML = `<strong>Level:</strong> ${npcData.level}`;
                        collapsibleContent.appendChild(levelInfo);

                        const hpInfo = document.createElement('p');
                        hpInfo.innerHTML = `<strong>HP:</strong> ${npcData.hp}`;
                        collapsibleContent.appendChild(hpInfo);

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
                const npcFullListElement = document.getElementById('npc-full-list');
                if (npcFullListElement) {
                    npcFullListElement.textContent = 'Failed to load NPC details.';
                }
            });
    }

    // Event listener for the generate NPCs button
    document.getElementById('generateNpcsBtn').addEventListener('click', fetchFullNpcDetails);

    // Function to toggle the visibility of all collapsible content
    function toggleAllCollapsible() {
        const allCollapsibleContent = document.querySelectorAll('.collapsible-content');
        let isAnyExpanded = Array.from(allCollapsibleContent).some(content => content.style.maxHeight !== '' && content.style.maxHeight !== '0px');

        allCollapsibleContent.forEach(content => {
            if (isAnyExpanded) {
                content.style.maxHeight = '0';
            } else {
                setTimeout(() => content.style.maxHeight = `${content.scrollHeight}px`, 10);
            }
        });
    }

    // Event listener for the toggle all button
    document.getElementById('toggleAll').addEventListener('click', toggleAllCollapsible);
});
