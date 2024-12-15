<template>
  <div class="container">
    <div class="form-wrapper">
      <h1 class="title">ScrapIt</h1>
      <p class="subtitle">Scrape emails and phone numbers with ease.</p>

      <form @submit.prevent="submitForm" class="form">
        <div class="form-group">
          <label for="interest">Interest:</label>
          <input
            type="text"
            id="interest"
            v-model="interest"
            placeholder="e.g., Marketing Manager"
            required
          />
        </div>

        <div class="form-group">
          <label for="country">Country:</label>
          <input
            type="text"
            id="country"
            v-model="country"
            placeholder="e.g., USA"
            required
          />
        </div>

        <button type="submit" class="btn-submit">Scrape</button>
      </form>
    </div>

    <div v-if="results.length > 0" class="results">
      <h2 class="results-title">Results</h2>
      <div class="results-grid">
        <div
          v-for="(result, index) in results"
          :key="index"
          class="result-card"
        >
          <p><strong>Name:</strong> {{ result.name }}</p>
          <p><strong>Emails:</strong> {{ result.emails.join(", ") }}</p>
          <p>
            <strong>Phone Numbers:</strong>
            {{ result.phone_numbers.join(", ") }}
          </p>
          <p>
            <strong>Source Link:</strong>
            <a :href="result.source_link" target="_blank">{{
              result.source_link
            }}</a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "SearchForm",
  data() {
    return {
      interest: "",
      country: "",
      results: [] as any[],
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await fetch("http://127.0.0.1:5000/scrape", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            interest: this.interest,
            country: this.country,
          }),
        });

        if (!response.ok) {
          throw new Error("Failed to fetch results.");
        }

        const data = await response.json();
        this.results = data.result || [];
      } catch (error: any) {
        alert(error.message || "Something went wrong.");
      }
    },
  },
});
</script>

<style lang="scss" scoped>
/* Global Container */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background: linear-gradient(to bottom right, #f7fafc, #edf2f7);
  min-height: 100vh;
  font-family: "Arial", sans-serif;
}

/* Form Section */
.form-wrapper {
  background: #ffffff;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 600px;
  width: 100%;
  margin: 0 auto;
}

.title {
  font-size: 2rem;
  font-weight: 700;
  color: #2d3748;
}

.subtitle {
  font-size: 1.2rem;
  color: #718096;
  margin-bottom: 1.5rem;
}

/* Form Styles */
.form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.form-group {
  width: 100%;
  display: flex;
  flex-direction: column;
  text-align: left;
}

label {
  font-size: 1rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #4a5568;
}

input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #cbd5e0;
  border-radius: 0.375rem;
  font-size: 1rem;
}

input:focus {
  border-color: #3182ce;
  outline: none;
  box-shadow: 0 0 0 2px rgba(49, 130, 206, 0.5);
}

.btn-submit {
  padding: 0.75rem 1.5rem;
  background: linear-gradient(to right, #3182ce, #63b3ed);
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.3s ease;
}

.btn-submit:hover {
  background: linear-gradient(to right, #2b6cb0, #4299e1);
}

/* Results Section */
.results {
  margin-top: 2rem;
  max-width: 900px;
  width: 100%;
  text-align: center;
}

.results-title {
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  color: #2d3748;
}

.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.result-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  padding: 1rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.result-card p {
  font-size: 1rem;
  margin-bottom: 0.5rem;
  color: #4a5568;
}

.result-card a {
  color: #3182ce;
  text-decoration: none;
}

.result-card a:hover {
  text-decoration: underline;
}
</style>
