<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="main bg-gradient-to-r from-blue-100 to-pink-100 min-h-screen">
        <!-- Navbar -->
        <nav class="flex justify-between items-center p-4 text-black shadow-md bg-white">
            <div class="flex items-center gap-2">
                <img src="https://imgs.search.brave.com/66yQEF01WsRh1ql1bZWJHMXeVvSUQP7LVjUFYgPEtr4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tYXJr/ZXRwbGFjZS5jYW52/YS5jb20vRUFFMEM0/UFFJMWsvMS8wLzE2/MDB3L2NhbnZhLWJp/a2UtbG9nby1YaWFv/NmhNSWhGTS5qcGc"
                    alt="Logo" class="h-14 w-14">
                <h2 class="text-2xl font-semibold">Karzo</h2>
            </div>
            <div class="hidden md:flex items-center gap-10 text-lg cursor-pointer">
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300">
                   <a href="#events">
                    Events
                   </a>
                </h3>
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300"><a href="#feedback">
                    Feedback
                   </a></h3>
                <h3 class="hover:text-gray-700 hover:-translate-y-3 transition duration-300"><a href="#blogs">
                    Blogs
                   </a></h3>
            </div>
            <div class="flex items-center gap-4">
                <RouterLink :to="{ name: 'DRegisterView' }">
                    <button
                        class="border-2 border-black text-black hover:border-slate-600 px-4 py-2 rounded-md hover:bg-pink-700 hover:text-white transition">Driver
                        Login/Signup</button>
                </RouterLink>
                <RouterLink :to="{ name: 'PRegisterView' }">
                    <button
                        class="border-2 border-black text-black hover:border-slate-600 px-4 py-2 rounded-md hover:bg-pink-700 hover:text-white transition">Passenger
                        Login/Signup</button>
                </RouterLink>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="flex flex-col lg:flex-row items-center justify-between p-6 lg:p-12 mx-auto max-w-7xl">

            <!-- Left Text Content -->
            <div class="max-w-md py-5">
                <h1 class="text-7xl font-bold mb-6 leading-tight">
                    KARZO <br> FOR EVENTS AND RIDES, FAST <br> RIDES.
                </h1>
                <p class="text-gray-600 mb-6">
                    Join productivity experts from around the world and receive WriteClick—the Karzo Blog Newsletter.
                </p>
                <div class="flex items-center gap-2">
                    <input type="email" placeholder="Enter email"
                        class="border border-gray-300 px-4 py-3 rounded-lg w-64">
                    <button class="bg-pink-500 text-white px-6 py-3 rounded-lg hover:bg-pink-600">Subscribe</button>
                </div>
            </div>

            <!-- Right Image Card -->
            <div class="lg:mt-0 max-w-xl">
                <div class="bg-white rounded-lg shadow-lg overflow-hidden">
                    <img src="https://imgs.search.brave.com/abP3g4dyrj_nzAIh_shkSn2pb_hK6jvcUupkrQ3_tqc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvODU3/NzE2NzcwL3Bob3Rv/L21hbi1yaWRpbmct/c2Nvb3Rlci1kdXJp/bmctc3Vuc2V0Lmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1f/TzBCbFFQTTNNTjBC/eHhEaWp5MXY4aWpf/d3BJTUxjSWVsa3A2/UVlCbU1rPQ" alt="Karzo Blog"
                        class="w-full">
                    <div class="p-4">
                        <h3 class="text-xl font-semibold">Post or book Ride through Events. Instant Ride Book.</h3>
                        <div class="flex items-center mt-2 text-gray-500 text-sm">
                            <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Author"
                                class="h-8 w-8 rounded-full mr-2">
                            <span>Zeb Evans</span>
                            <span class="ml-auto flex items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none"
                                    viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 8v4l3 3"></path>
                                </svg>
                                Max 1 min read
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Articles Section -->
        <section class="p-10" id="events">
            <h2 class="flex items-center text-2xl font-semibold gap-3 ">
                <i class="fa-regular fa-map bg-pink-500 p-4 rounded-2xl"></i>
                Top Events
            </h2>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mt-6">
                <!-- First Row -->
                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/7mdeEijBoPN_8xOoCTZb116QmK2nTEGhvOdx3yoCYNI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTU3/NTI1NTY3L3Bob3Rv/L2Jpa2VyLW91dC1m/b3ItYS1yaWRlLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1v/dDlSUUdyMG9oT21R/SFFNbUExeHlZclU2/bzJ4VGN3a3g5eXNX/Q0k0QW1VPQ"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">Churchgate</p>
                        <h3 class="text-xl font-bold mt-2">Kala Ghoda Fest</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/ijTo77se1G_-_xT2NtVZcQtEbTCp9SFN-grP6nUPSP0/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTEz/NjQxMzIxNS9waG90/by95b3VuZy1tYW4t/YXQtc3RyZWV0LW1h/cmtldC5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9b2JuYVI1/SUlJMGpSeEhLZDRa/UGwzTFJDMnBJNzky/S2JIWVIyZUJ6S0tl/OD0"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/-yO3Y6K6nhWpkIbxYdZnmUx1o_DISL_MOYcBoB6AA-k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAxNi8w/Mi8xMy8xMy8xMS9v/bGR0aW1lci0xMTk3/ODAwXzY0MC5qcGc"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">Dadar</p>
                        <h3 class="text-xl font-bold mt-2">Shivaji park diwali festival.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/ZwaaoEqTuikuekr7KJS8-VQdgt2DpEDk3ZdNf1L0AxI/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvOTU4/MDY0MjI4L3Bob3Rv/L3BvcnRyYWl0LW9m/LWhhcHB5LXlvdW5n/LW1hbi5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9bFpveEFH/d1FkX0lMMXA1MFI2/RkNYd2JLdG9mb1N1/a25tQUtKb2Q2T2t6/UT0"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/fem6_chcVwffrqdRfXHJuTBm38x0NI3s4z3yvukVqGs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNTIx/ODkwMzI5L3Bob3Rv/L2Jpa2UtcmlkZXIu/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PXA1Nkp4eGlDWDNM/eU1zdWZFNXVtUi1r/V1FrUHNiUm5POEtJ/OUpyamgxUFk9"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">Mahim</p>
                        <h3 class="text-xl font-bold mt-2">Mahim ka mela.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/KUtv8_2I1cc7cEGCu4UanWs03EhmNRjVqqabwpWLbLM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTQ1/NTM0MzI4Mi9waG90/by92aWRlby1wb3J0/cmFpdC1vZi1hbi1p/bmRpYW4tbWFuLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1X/dUZkWlpTQ2N2c2h0/LVV5aWwtXzItY3pt/ZkplV2Nmd25FNlRf/bmNKTHZZPQ"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Second Row -->
                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/ErhPvm2aFdg3QMd1UjOEZcl8mY6GHbLl6H6EpRzMYqc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTU2/MTUyODg2L3Bob3Rv/L21vdG9yYmlrZS1y/aWRlLW9uLWEtY291/bnRyeS1yb2FkLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1x/OTFkU2QtdzExMGVo/RzFHT0dvemJ0SktK/M2R6TTdfem1aUnJ6/LTZGNXo4PQ"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">Bandra</p>
                        <h3 class="text-xl font-bold mt-2">Bandra Bandstand and reclamation.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/RFz5A_fbumGYi9OWZLxAFJrWjoaymucnmINdmpufADQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTEy/ODY3ODk4Ni9waG90/by9wb3J0cmFpdC1v/Zi1hLWhhbmRzb21l/LWluZGlhbi1tYW4u/anBnP3M9NjEyeDYx/MiZ3PTAmaz0yMCZj/PXQ1Y09UdkVCVl9f/NG1TeUZpR1IyMk53/REZHeElldUdkeXIy/c05RODAtNGs9"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/liQxq7ICPU7J4N5PaG6fQqm5j4vfPQebQ6P3JK4XR_M/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTU4/MjY2NDgzMS9waG90/by9iaWtlci13aXRo/LWZ1bGwtc2FmZXR5/LWdlYXItZW5qb3lz/LXJpZGUtb24tY291/bnRyeS1yb2FkLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz0x/R1VRVjlpWnh4OU5I/MTk0U19RWlJRenNq/YkhndDBTZ29CN01Y/Y1dKTEM0PQ"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">Ghatkoper</p>
                        <h3 class="text-xl font-bold mt-2">Tata Running race.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/AEvxdXin6oXW-2zSlMBH26tndkwHCAJNVK100zPhA2g/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTMw/MDMxOTcxMy9waG90/by9wb3J0cmFpdC1v/Zi1tYW4taW4tdHJh/ZGl0aW9uYWwtaW5k/aWFuLWNsb3RoaW5n/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1IREF6dXhOVmpw/VEZveE15ODctSldX/VXZ4ajVzb1d3YjAy/ZVNTOXE1NE0wPQ"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>

                <div class="bg-white shadow-lg rounded-xl overflow-hidden">
                    <img src="https://imgs.search.brave.com/OUe16QaKAAoF4uI3mqk8XrYozmpIPy_BweBt_eZZpxE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNjI1/ODMwMDUwL3Bob3Rv/L21vdG9yY3ljbGUt/cGFya2luZy1zcGFj/ZS1pbi1pbmRpYS5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/bXlHZ1lsNy1iZ1R5/Y29tTW5aLUdobEdJ/ZDlxMm0wa21WMFVk/VGxELVl3TT0"
                        alt="Article Image" class="w-full">
                    <div class="p-6">
                        <p class="text-pink-500 font-semibold text-sm">Goa</p>
                        <h3 class="text-xl font-bold mt-2">St.Vectoria Church.</h3>
                        <div class="flex items-center mt-4">
                            <img src="https://imgs.search.brave.com/-JpHJukojOqSZvREizeH89q6TDHhRR7wn4S0vucgeb8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by9p/bmRpYW4tbWFuLWNp/dHktbWFsZS10cmFk/aXRpb25hbC10dXJi/YW4taGluZHVpc3Qt/c3VtbWVyLWNpdHlf/MTE1Ny00MTAyNi5q/cGc_c2VtdD1haXNf/aHlicmlk"
                                alt="Author" class="w-8 h-8 rounded-full">
                            <p class="ml-2 text-gray-600">Zeb Evans</p>
                            <span class="ml-auto flex items-center text-gray-500">

                                Max 1min read
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            
        </section>

<!-- User Feedback Section -->
<section class="p-10 pt-12 pb-15" id="feedback">
  <div class="text-center py-10 max-w-5xl mx-auto">
    <h2 class="text-black text-lg font-bold">User Feedback</h2>
    <h1 class="text-3xl md:text-4xl font-bold mt-2">
      What Karzo users are saying about their ride experience.
    </h1>
    <p class="text-gray-600 mt-3">
      Karzo is committed to providing a seamless and reliable ridesharing experience.
      See what our users have to say about their journeys with us!
    </p>
  </div>
  <div class="feedback-container overflow-hidden w-full">
    <div
      class="feedback-scroll flex gap-6 w-max animate-[scroll_15s_linear_infinite]"
    >
      <!-- Feedback Items -->
      <div class="flex gap-6">
        <div
          class="p-5 shadow-lg rounded-lg bg-gray-50 flex flex-col items-center"
        >
          <img
            src="https://randomuser.me/api/portraits/men/7.jpg"
            class="w-12 h-12 rounded-full"
            alt="User"
          />
          <h4 class="text-lg font-semibold">Rahul Sharma</h4>
          <p class="text-yellow-500">
            <i class="fa-solid fa-star"></i> 4.8
          </p>
          <p class="text-gray-600">
            Karzo makes commuting so easy! The multi-stop feature is a lifesaver.
          </p>
        </div>
        <div
          class="p-5 shadow-lg rounded-lg bg-gray-50 flex flex-col items-center"
        >
          <img
            src="https://randomuser.me/api/portraits/women/8.jpg"
            class="w-12 h-12 rounded-full"
            alt="User"
          />
          <h4 class="text-lg font-semibold">Ananya Verma</h4>
          <p class="text-yellow-500">
            <i class="fa-solid fa-star"></i> 5.0
          </p>
          <p class="text-gray-600">
            Love the safety gear reminders and ride experience ratings!
          </p>
        </div>
        <div
          class="p-5 shadow-lg rounded-lg bg-gray-50 flex flex-col items-center"
        >
          <img
            src="https://randomuser.me/api/portraits/men/9.jpg"
            class="w-12 h-12 rounded-full"
            alt="User"
          />
          <h4 class="text-lg font-semibold">Vikram Patel</h4>
          <p class="text-yellow-500">
            <i class="fa-solid fa-star"></i> 4.7
          </p>
          <p class="text-gray-600">
            The shared taxi option is great for saving money on daily rides!
          </p>
        </div>
        <div
          class="p-5 shadow-lg rounded-lg bg-gray-50 flex flex-col items-center"
        >
          <img
            src="https://randomuser.me/api/portraits/women/10.jpg"
            class="w-12 h-12 rounded-full"
            alt="User"
          />
          <h4 class="text-lg font-semibold">Meera Nair</h4>
          <p class="text-yellow-500">
            <i class="fa-solid fa-star"></i> 4.9
          </p>
          <p class="text-gray-600">
            Booking is super fast and the drivers are friendly. Great experience!
          </p>
        </div>
      </div>
      <!-- Duplicate Items for Infinite Scroll Effect -->
      <div class="flex gap-6">
        <div
          class="p-5 shadow-lg rounded-lg bg-gray-50 flex flex-col items-center"
        >
          <img
            src="https://randomuser.me/api/portraits/men/7.jpg"
            class="w-12 h-12 rounded-full"
            alt="User"
          />
          <h4 class="text-lg font-semibold">Rahul Sharma</h4>
          <p class="text-yellow-500">
            <i class="fa-solid fa-star"></i> 4.8
          </p>
          <p class="text-gray-600">
            Karzo makes commuting so easy! The multi-stop feature is a lifesaver.
          </p>
        </div>
        <div
          class="p-5 shadow-lg rounded-lg bg-gray-50 flex flex-col items-center"
        >
          <img
            src="https://randomuser.me/api/portraits/women/8.jpg"
            class="w-12 h-12 rounded-full"
            alt="User"
          />
          <h4 class="text-lg font-semibold">Ananya Verma</h4>
          <p class="text-yellow-500">
            <i class="fa-solid fa-star"></i> 5.0
          </p>
          <p class="text-gray-600">
            Love the safety gear reminders and ride experience ratings!
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

        <section class="p-10 lg:p-20 text-center relative" id="blogs">
            <h2 class="text-3xl font-bold mb-6">Latest Blogs & Insights</h2>
            <p class="text-lg text-gray-600 mb-10">
                Stay updated with expert opinions, industry trends, and the latest news from our team.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Blog 1 -->
                <div
                    class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
                    <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ"
                        alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
                    <div class="p-6 text-left">
                        <h3 class="text-xl font-semibold">The Future of Ridesharing</h3>
                        <p class="text-gray-600 mt-2">
                            The ridesharing industry is evolving rapidly with AI and electric vehicles playing a major
                            role.
                            Companies are focusing on safety measures, eco-friendly rides, and seamless customer
                            experiences.
                            As urban mobility demands grow, integrating smart technology will be crucial for the next
                            phase of ridesharing.
                        </p>
                        <p class="text-gray-500 text-sm mt-2">😄 By John Doe | March 10, 2025</p>
                    </div>
                </div>

                <!-- Blog 2 -->
                <div
                    class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
                    <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ"
                        alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
                    <div class="p-6 text-left">
                        <h3 class="text-xl font-semibold">Smart City Transportation</h3>
                        <p class="text-gray-600 mt-2">
                            Smart cities are integrating intelligent transportation systems to reduce congestion and
                            pollution.
                            Automated public transport, data-driven traffic management, and sustainable ride options are
                            shaping urban mobility.
                            The future holds AI-driven solutions that will make commuting more efficient and affordable.
                        </p>
                        <p class="text-gray-500 text-sm mt-2">😄 By Jane Smith | March 8, 2025</p>
                    </div>
                </div>

                <!-- Blog 3 -->
                <div
                    class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
                    <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ"
                        alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
                    <div class="p-6 text-left">
                        <h3 class="text-xl font-semibold">Maximizing Driver Earnings</h3>
                        <p class="text-gray-600 mt-2">
                            Rideshare drivers can increase earnings by optimizing their working hours, choosing
                            high-demand locations, and utilizing incentives.
                            Learning passenger trends and leveraging in-app features help maximize efficiency.
                            Future trends suggest better pay models and benefits for rideshare drivers.
                        </p>
                        <p class="text-gray-500 text-sm mt-2">😄 By Alex Brown | March 5, 2025</p>
                    </div>
                </div>

                <!-- Blog 4 -->
                <div
                    class="flex flex-col md:flex-row items-center border-2 border-gray-400 backdrop-blur-md p-6 rounded-lg shadow-xl">
                    <img src="https://imgs.search.brave.com/59qNrg_Isrs2nR6cV81iim8DTN58A6bNxJvBvTmu_YE/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvNjUx/MjcwMzExL3Bob3Rv/L2NoaGF0cmFwYXRp/LXNoaXZhamktcmFp/bHdheS1zdGF0aW9u/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz1JblF0a3NpTnkx/aC11czBlcFc1Wl94/STJzQzh2VDhvWE5s/d002cjVuc0VvPQ"
                        alt="Blog Image" class="w-full md:w-1/2 h-56 object-cover rounded-lg">
                    <div class="p-6 text-left">
                        <h3 class="text-xl font-semibold">Ridesharing vs Traditional Taxis</h3>
                        <p class="text-gray-600 mt-2">
                            While traditional taxis have long been a reliable mode of transport, ridesharing apps offer
                            flexibility, affordability, and real-time tracking.
                            The competition is leading to improved services, but regulatory challenges remain a key
                            factor.
                            Passenger safety, pricing models, and driver benefits are crucial in shaping the industry's
                            future.
                        </p>
                        <p class="text-gray-500 text-sm mt-2">😄 By Lisa Green | March 2, 2025</p>
                    </div>
                </div>
            </div>
        </section>
        <footer class="bg-gray-100 py-8">
            <div class="container mx-auto px-6">
                <div class="grid md:grid-cols-3 gap-8">

                    <!-- Left Section -->
                    <div>
                        <h2 class="text-lg font-semibold text-gray-800">Let's keep in touch!</h2>
                        <p class="text-gray-600 mt-1">Find us on any of these platforms, we respond in 1-2 business
                            days.</p>

                        <!-- Social Icons -->
                        <div class="flex space-x-3 mt-4">
                            <a href="#"
                                class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md hover:bg-gray-200">
                                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/twitter.svg"
                                    class="w-5 h-5" alt="Twitter">
                            </a>
                            <a href="#"
                                class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md hover:bg-gray-200">
                                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/facebook.svg"
                                    class="w-5 h-5" alt="Facebook">
                            </a>
                            <a href="#"
                                class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md hover:bg-gray-200">
                                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/dribbble.svg"
                                    class="w-5 h-5" alt="Dribbble">
                            </a>
                            <a href="#"
                                class="w-10 h-10 bg-white rounded-full flex items-center justify-center shadow-md hover:bg-gray-200">
                                <img src="https://cdn.jsdelivr.net/npm/simple-icons@v6/icons/github.svg" class="w-5 h-5"
                                    alt="GitHub">
                            </a>
                        </div>
                    </div>

                    <!-- Middle Section -->
                    <div>
                        <h2 class="text-lg font-semibold text-gray-800">USEFUL LINKS</h2>
                        <ul class="mt-2 space-y-1 text-gray-600">
                            <li><a href="#" class="hover:text-gray-800">Blog</a></li>
                            <li><a href="#" class="hover:text-gray-800">Github</a></li>
                        </ul>
                    </div>

                    <!-- Right Section -->
                    <div>
                        <h2 class="text-lg font-semibold text-gray-800">OTHER RESOURCES</h2>
                        <ul class="mt-2 space-y-1 text-gray-600">
                            <li><a href="#" class="hover:text-gray-800">MIT License</a></li>
                            <li><a href="#" class="hover:text-gray-800">Terms & Conditions</a></li>
                            <li><a href="#" class="hover:text-gray-800">Privacy Policy</a></li>
                            <li><a href="#" class="hover:text-gray-800">Contact Us</a></li>
                        </ul>
                    </div>

                </div>

                <!-- Copyright -->
                <div class="text-center text-gray-600 text-sm mt-8">
                    Copyright © 2025 KARZO Website by Yash Patkar.
                </div>
            </div>
        </footer>

    </div>
</template>

<style>
@keyframes scroll {
    from {
        transform: translateX(0);
    }

    to {
        transform: translateX(-50%);
    }
}

.animate-scroll {
    display: flex;
    width: max-content;
    animation: scroll 15s linear infinite;
}
</style>