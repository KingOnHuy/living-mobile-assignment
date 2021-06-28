import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "../store"

Vue.use(VueRouter);

function loadView(name) {
  return import(`../views/${name}`);
}

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/store",
    name: "Store",
    component: () => loadView("Store"),
  },
  {
    path: "/category",
    name: "Category",
    component: () => loadView("Category"),
  },
  {
    path: "/menu",
    name: "Menu",
    component: () => loadView("Menu"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => loadView("Login"),
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});
// eslint-disable-next-line no-unused-vars
router.beforeEach((to, from, next) => {
  if (to.name !== "Login" && store.getters["auth/isLogin"]) {
    next();
  } else if (to.name === "Login") {
    next();
  }
  if (to.name !== "Login") {
    next({ name: "Login" });
  }
});

export default router;
