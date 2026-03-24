#!/usr/bin/env python3
"""
代理测试脚本示例
测试单个代理的连通性和延迟，输出结果到标准输出或CSV。
用法：python test_proxy.py --proxy http://user:pass@ip:port --target http://httpbin.org/ip
"""

import argparse
import requests
import time

def test_proxy(proxy_url, target_url, timeout=10):
    """测试代理是否可用，返回状态码、耗时和错误信息"""
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    start = time.time()
    try:
        resp = requests.get(target_url, proxies=proxies, timeout=timeout)
        elapsed = time.time() - start
        return resp.status_code, elapsed, None
    except Exception as e:
        elapsed = time.time() - start
        return None, elapsed, str(e)

def main():
    parser = argparse.ArgumentParser(description="测试代理连通性")
    parser.add_argument("--proxy", required=True, help="代理URL，格式：http://user:pass@ip:port")
    parser.add_argument("--target", default="http://httpbin.org/ip", help="测试目标URL")
    parser.add_argument("--timeout", type=int, default=10, help="超时时间（秒）")
    args = parser.parse_args()

    status, elapsed, err = test_proxy(args.proxy, args.target, args.timeout)
    print(f"代理: {args.proxy}")
    print(f"目标: {args.target}")
    if status:
        print(f"状态码: {status}, 耗时: {elapsed:.3f}s")
    else:
        print(f"失败: {err}, 耗时: {elapsed:.3f}s")

if __name__ == "__main__":
    main()
