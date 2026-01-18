interface CreateNotificationPayload {
  message: string;
  type?: string;
}

export const createNotification = async (
  payload: CreateNotificationPayload
) => {
  const res = await fetch("http://127.0.0.1:8000/notification", {
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
  const res = await fetch("http://127.0.0.1:8000/notification", {
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
