import { API_BASE_URL } from "../settings";

interface CreateNotificationPayload {
  message: string;
  type?: string;
}

export const createNotification = async (
  payload: CreateNotificationPayload
) => {
  const res = await fetch(`${API_BASE_URL}/notification`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("Failed to create notification");
  }

  return await res.json();
};

export const fetchNotifications = async () => {
  const res = await fetch(`${API_BASE_URL}/notification`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!res.ok) {
    throw new Error("Failed to fetch notifications");
  }

  return await res.json();
};
