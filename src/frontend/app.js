const API_URL = "http://localhost:8000/api/policies";

async function loadPolicies(status = "") {

    let url = API_URL;

    if (status) {
        url += `?status=${status}`;
    }

    const response = await fetch(url);

    const policies = await response.json();

    renderPolicies(policies);
}

function renderPolicies(policies) {

    const tbody =
        document.getElementById("policies-body");

    tbody.innerHTML = "";
    
    document.getElementById(
        "policy-count"
    ).innerText =
        `Pólizas encontradas: ${policies.length}`;

    policies.forEach(policy => {

        const days =
            calculateDaysRemaining(
                policy.expiration_date
            );

        const row =
            document.createElement("tr");

        row.innerHTML = `
            <td>${policy.client_id}</td>

            <td>${policy.policy_number}</td>

            <td>${policy.policy_type}</td>

            <td>${policy.expiration_date}</td>

            <td>${days}</td>

            <td>
                <span class="${getStatusClass(policy.status)}">
                    ${policy.status}
                </span>
            </td>

            <td>
                <button onclick="openRenewModal(${policy.id})">
                    Renovar
                </button>
            </td>
        `;

        tbody.appendChild(row);

    });
}


function calculateDaysRemaining(expirationDate) {

    const today = new Date();

    const expiration = new Date(expirationDate);

    const diffTime = expiration - today;

    return Math.ceil(
        diffTime / (1000 * 60 * 60 * 24)
    );
}


async function openRenewModal(policyId) {

    const newDate = prompt(
        "Ingrese la nueva fecha de vencimiento (YYYY-MM-DD):"
    );

    if (!newDate) {
        return;
    }

    try {

        const response = await fetch(
            `http://localhost:8000/api/policies/${policyId}/renew`,
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    new_expiration_date: newDate
                })
            }
        );

        const result = await response.json();

        alert(result.message);

        loadPolicies();

    } catch (error) {

        console.error(error);

        alert("Error al renovar la póliza");
    }
}


function getStatusClass(status) {

    switch(status) {

        case "upcoming":
            return "upcoming";

        case "renewable":
            return "renewable";

        case "lost":
            return "lost";

        case "renewed":
            return "renewed";

        default:
            return "";
    }
}

loadPolicies();