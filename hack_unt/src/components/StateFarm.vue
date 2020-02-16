<template>
  <v-app>
    <v-card class="ma-5">
      <v-toolbar prominent elevated>
        <v-toolbar-title>Cardiovascular Health Tracker Powered by Fitbit</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-img
            class="mr-3"
            src="https://1000logos.net/wp-content/uploads/2018/03/State-Farm-Logo-768x432.png"
            height="100px"
            width="180px"
          ></v-img>
        </v-toolbar-items>
      </v-toolbar>
    </v-card>

    <v-card class="mx-5">
      <v-row>
        <v-col cols="6">
          <v-card-title>Austin Hwang</v-card-title>
          <v-card-subtitle>Policy Number: 0123adf83</v-card-subtitle>
          <v-card-text>Current Premium: $245.43 Next Billing Date: 03/05/2020</v-card-text>
        </v-col>
      </v-row>
    </v-card>

    <v-card class="ma-5">
      <v-row>
        <v-col cols="2">
          <v-card-title>Fitbit Data</v-card-title>
        </v-col>
        <v-col cols="10">
          <v-img
            contain
            class="mr-3"
            src="data:image/png;base64,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"
            height="50px"
            width="180px"
          ></v-img>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="6">
          <v-card-text>
            <p>Age: {{age}}</p>
            <p>Gender: {{gender}}</p>
            <p>Height: {{height}}</p>
            <p>Weight: {{weight}}</p>
            <p>BMI: {{bmi}}</p>
          </v-card-text>
        </v-col>
        <v-col cols="6">
          <v-card-text>
            <p>Average Miinutes of Activity: {{minutesActive}} /day</p>
            <p>Blood Pressure (Diastolic/Systolic): {{bp[1]}} / {{bp[2]}} mmHg</p>
            <p>Blood Glucose: {{glucose}} mg/dL</p>
            <p>Cholesterol (LDL): {{cholesterol}} mg/dL</p>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>

    <v-card class="mx-5">
      <v-card-title>My Progress Towards Premium Savings</v-card-title>
      <v-progress-linear color="light-blue" height="10" value="10" striped></v-progress-linear>

      <v-card-actions>
        <v-btn class="ma-5" v-on:click="onSubmit">Compute My Score for Cardiovascular Health</v-btn>
        <v-btn class="ma-5" v-on:click="getFitbit">Sync with My Fitbit Account</v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      age: 21,
      gender: "Male",
      height: 5,
      weight: 165,
      bmi: 27.14,
      minutesActive: 105,
      bp: [125, 75],
      glucose: 5,
      cholesterol: 180,
      test_data: [
        72726,
        1,
        172,
        95,
        160.0,
        100.0,
        1.0,
        1.0,
        0.0,
        0.0,
        1.0,
        32.111952
      ]
    };
  },
  methods: {
    getFitbit: function() {
      axios
        .get("http://localhost:5000/get_fitbit_data")
        .then(res => {
          this.minutesActive = res.minutesActive;
          this.bmi = res.bmi;
          this.weight = res.weight;
          this.weight = res.height;
        })
        .catch(error => {
          console.log(error);
        });
    },
    getPredictions: function(payload) {
      console.log("hi");
      axios
        .post("http://localhost:5000/get_predictions", payload)
        .then(res => {
          this.score = res.score;
        })
        .catch(error => {
          console.log(error);
        });
    },
    onSubmit: function() {
      console.log("hi");
      let payload = {
          test_data: this.test_data
      }
      this.getPredictions(payload);
    }
  },
  created() {
    this.getFitbit();
  }
};
</script>