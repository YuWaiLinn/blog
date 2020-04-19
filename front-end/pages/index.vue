<template>
  <main class="container mt-5">
    <div class="row">
      <!-- <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>La Recipes</h3>
          <nuxt-link to="/recipes/add" class="btn btn-info">Add Recipe</nuxt-link>
        </div>
      </div> -->
      <!-- {{ products }} -->
      <template v-for="product in products">
        <div :key="product.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <!-- <product-card :onDelete="deleteRecipe" :recipe="product"></product-card> -->
          <product-card :product="product"></product-card>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import ProductCard from "~/components/ProductCard.vue";

export default {
  components: {
    ProductCard
  },
  data() {
    return {
      products: []
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let response = await $axios.$get(`/products/product_list/`);
      let products = response;
      return { products: products };
    } catch (e) {
      return { products: [] };
    }
  }
};
</script>
