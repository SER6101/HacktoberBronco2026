const ACCOUNTS_KEY = "hobbob.demo.accounts";
const ACTIVE_ACCOUNT_KEY = "hobbob.demo.active";

function readAccounts() {
  return JSON.parse(localStorage.getItem(ACCOUNTS_KEY) || "{}");
}

export function getActiveUser() {
  const email = localStorage.getItem(ACTIVE_ACCOUNT_KEY);
  return email ? readAccounts()[email] || null : null;
}

export function createDemoUser({ name, email }) {
  const normalizedEmail = email.trim().toLowerCase();
  const accounts = readAccounts();
  if (accounts[normalizedEmail]) {
    throw new Error("That email already has a demo profile. Try logging in.");
  }

  const user = {
    name: name.trim(),
    email: normalizedEmail,
    answers: null,
    hobbies: [],
    progress: {},
    skillLevels: {},
  };
  accounts[normalizedEmail] = user;
  localStorage.setItem(ACCOUNTS_KEY, JSON.stringify(accounts));
  localStorage.setItem(ACTIVE_ACCOUNT_KEY, normalizedEmail);
  return user;
}

export function loginDemoUser(email) {
  const normalizedEmail = email.trim().toLowerCase();
  const user = readAccounts()[normalizedEmail];
  if (!user) {
    throw new Error("No demo profile found for that email. Create an account first.");
  }
  localStorage.setItem(ACTIVE_ACCOUNT_KEY, normalizedEmail);
  return user;
}

export function saveDemoUser(user) {
  const accounts = readAccounts();
  accounts[user.email] = user;
  localStorage.setItem(ACCOUNTS_KEY, JSON.stringify(accounts));
  localStorage.setItem(ACTIVE_ACCOUNT_KEY, user.email);
  return user;
}

export function logoutDemoUser() {
  localStorage.removeItem(ACTIVE_ACCOUNT_KEY);
}
