FROM mcr.microsoft.com/playwright:v1.44.1-jammy
WORKDIR /tests
COPY . .
RUN npm install
CMD ["npx", "playwright", "test"]