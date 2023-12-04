/*
 * :file description:
 * :name: /intelligent/app/layout.tsx
 * :author: 张德志
 * :copyright: (c) 2023, Tungee
 * :date created: 2023-09-21 06:56:40
 * :last editor: 张德志
 * :date last edited: 2023-12-04 20:54:28
 */
/* eslint-disable @next/next/no-page-custom-font */
import "./styles/globals.scss";
import "./styles/markdown.scss";
import "./styles/highlight.scss";
import { Providers } from "./providers";
import { getClientConfig } from "./config/client";
import { type Metadata } from "next";

export const metadata: Metadata = {
  title: "晓智gpt",
  description: "构建您的私人助理",
  viewport: {
    width: "device-width",
    initialScale: 1,
    maximumScale: 1,
  },
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#fafafa" },
    { media: "(prefers-color-scheme: dark)", color: "#151515" },
  ],
  appleWebApp: {
    title: "晓智gpt",
    statusBarStyle: "default",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="zh">
      <head>
        <meta name="config" content={JSON.stringify(getClientConfig())} />
        <link rel="manifest" href="/site.webmanifest"></link>
        <script src="/serviceWorkerRegister.js" defer></script>
      </head>
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
