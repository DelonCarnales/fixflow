function getApiBase() {
  const host = window.location.hostname;
  const codespaceMatch = host.match(/^(.*)-5173\.app\.github\.dev$/);

  if (codespaceMatch) {
    // The frontend and backend use separate forwarded ports in GitHub Codespaces.
    return window.location.protocol + "//" + codespaceMatch[1] + "-8000.app.github.dev";
  }

  // Local Mac/PC development.
  return "http://127.0.0.1:8000";
}

const API_BASE = getApiBase();

async function request(path, options = {}) {
  const response = await fetch(API_BASE + path, {
    ...options,
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
  });

  let data = null;
  try {
    data = await response.json();
  } catch {
    // Some error responses do not contain JSON.
  }

  if (!response.ok) {
    const message = data && data.detail
      ? (typeof data.detail === "string" ? data.detail : "The request data is invalid.")
      : "The backend request failed.";
    const error = new Error(message);
    error.status = response.status;
    throw error;
  }

  return data;
}

export async function listOrders() {
  return request("/orders");
}

export async function listParts() {
  return request("/parts");
}

export async function createOrder(input) {
  return request("/orders", {
    method: "POST",
    body: JSON.stringify(input),
  });
}

export async function updateOrder(id, input) {
  return request("/orders/" + encodeURIComponent(id), {
    method: "PATCH",
    body: JSON.stringify(input),
  });
}

export async function updateOrderStatus(id, status) {
  return request("/orders/" + encodeURIComponent(id) + "/status", {
    method: "PATCH",
    body: JSON.stringify({ status }),
  });
}

export async function savePart(id, input) {
  if (id) {
    return request("/parts/" + encodeURIComponent(id), {
      method: "PATCH",
      body: JSON.stringify(input),
    });
  }

  return request("/parts", {
    method: "POST",
    body: JSON.stringify(input),
  });
}

export async function getPublicOrderStatus(id) {
  try {
    return await request("/public/orders/" + encodeURIComponent(id));
  } catch (error) {
    if (error.status === 404) return null;
    throw error;
  }
}
