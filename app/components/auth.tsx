/*
 * :file description: 
 * :name: /intelligent/app/components/auth.tsx
 * :author: 张德志
 * :copyright: (c) 2023, Tungee
 * :date created: 2023-09-20 09:01:06
 * :last editor: 张德志
 * :date last edited: 2023-12-04 20:47:52
 */
import styles from "./auth.module.scss";
import { IconButton } from "./button";
import {Button} from '@nextui-org/button'; 
import { useNavigate } from "react-router-dom";
import { Path } from "../constant";
import { useAccessStore } from "../store";
import Locale from "../locales";
import BotIcon from "../icons/bot.svg";
import { useEffect } from "react";
import { getClientConfig } from "../config/client";

export function AuthPage() {
  const navigate = useNavigate();
  const access = useAccessStore();

  const goHome = () => navigate(Path.Home);
  const resetAccessCode = () => access.updateCode(""); // Reset access code to empty string

  useEffect(() => {
    if (getClientConfig()?.isApp) {
      navigate(Path.Settings);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className={styles["auth-page"]}>
      <div className={`no-dark ${styles["auth-logo"]}`}>
        <BotIcon />
      </div>

      <div className={styles["auth-title"]}>{Locale.Auth.Title}</div>
      <div className={styles["auth-tips"]}>{Locale.Auth.Tips}</div>
    <Button>HELLO WORLD</Button>
      <input
        className={styles["auth-input"]}
        type="password"
        placeholder={Locale.Auth.Input}
        value={access.accessCode}
        onChange={(e) => {
          access.updateCode(e.currentTarget.value);
        }}
      />

      <div className={styles["auth-actions"]}>
        <IconButton
          text={Locale.Auth.Confirm}
          type="primary"
          onClick={goHome}
        />
        <IconButton text={Locale.Auth.Later} onClick={() => {
          resetAccessCode();
          goHome();
        }} />
      </div>
    </div>
  );
}
